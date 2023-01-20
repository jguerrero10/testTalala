from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import AnonymousUser, Group
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from rest_framework.authentication import BasicAuthentication
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from civiapp.forms import OfficerForm, OfficerUpdateForm
from civiapp.models import Citation, Clerk, Officer
from civiapp.serializers import CitationSerializer


class CitationView(CreateModelMixin, GenericViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CitationSerializer
    queryset = Citation.objects.all()

    def perform_create(self, serializer):
        officer = Officer.objects.get(user=self.request.user)
        serializer.save(officer=officer)


@login_required(login_url='/login/')
@permission_required('civiapp.view_citation', raise_exception=True)
def list_citations(request):
    context = dict()
    try:
        clerk = Clerk.objects.get(user=request.user)
        citations = Citation.objects.select_related('officer__agency').filter(officer__agency=clerk.agency)
    except ObjectDoesNotExist:
        if Officer.objects.filter(user=request.user):
            citations = Citation.objects.select_related('officer').filter(officer__user=request.user)
        else:
            citations = Citation.objects.all()
    context['citations'] = citations
    return render(request, 'citation/index.html', context)


@login_required(login_url='/login/')
@permission_required('view_citation', raise_exception=True)
def detail_citation(request, id):
    citation = Citation.objects.get(id=id)
    return render(request, 'citation/detail.html', {'citation': citation})


def home(request):
    is_officer = False
    if not isinstance(request.user, AnonymousUser):
        if Officer.objects.filter(user=request.user):
            is_officer = True
    return render(request, 'home.html', {'is_officer': is_officer})


def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("Error Login")
    else:
        return render(request, 'login/login.html')


@login_required(login_url='/login/')
def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
@permission_required('civiapp.view_officer', raise_exception=True)
def list_officer(request):
    if Clerk.objects.filter(user=request.user):
        officers = Officer.objects.all().filter(agency__clrek_agency__user=request.user)
    else:
        officers = Officer.objects.all()
    context = {
        'officers': officers
    }
    return render(request, 'officer/index.html', context)


@login_required(login_url='/login/')
@permission_required('civiapp.add_officer', raise_exception=True)
def create_officer(request):
    if request.method == 'POST':
        form = OfficerForm(request.POST)
        if form.is_valid():
            badge = form.cleaned_data['badge']
            clerk = Clerk.objects.select_related('agency').get(user=request.user)
            user = form.save()
            user.groups.add(Group.objects.get(name='OFFICER'))
            officer = Officer.objects.create(user=user, badge=badge, agency=clerk.agency)
            return JsonResponse({
                'error': 'success',
                'title': 'Success',
                'message': f'Officer {officer.user} is saved'

            })
        else:
            return JsonResponse({
                'error': 'error',
                'title': 'Error',
                'message': 'Error'
            })
    else:
        context = {'form': OfficerForm()}
        return render(request, 'officer/create.html', context)


@login_required(login_url='/login/')
@permission_required('civiapp.change_officer', raise_exception=True)
def update_officer(request, id):
    try:
        officer = Officer.objects.get(id=id)
        if request.method == 'POST':
            form = OfficerUpdateForm(request.POST, instance=officer.user)
            if form.is_valid():
                badge = form.cleaned_data['badge']
                form.save()
                officer.badge = badge
                officer.save()
                return JsonResponse({
                    'error': 'success',
                    'title': 'Success',
                    'message': f'Officer {officer.user} is saved'
                })
            else:
                return JsonResponse({
                    'error': 'error',
                    'title': 'Error',
                    'message': 'Error'})
        else:
            context = {
                'form': OfficerUpdateForm(instance=officer.user),
                'officer': officer
            }
            return render(request, 'officer/update.html', context)
    except ObjectDoesNotExist:
        return HttpResponse('No existe el Objeto')


@login_required(login_url='/login/')
@permission_required('civiapp.delete_officer', raise_exception=True)
def delete_officer(request, id):
    try:
        officer = Officer.objects.get(id=id)
        officer.delete()
        return HttpResponseRedirect(reverse('list-officer'))
    except ObjectDoesNotExist:
        return HttpResponse('No existe el Objeto')


@login_required(login_url='/login/')
@permission_required('civiapp.view_officer', raise_exception=True)
def detail_officer(request):
    context = {
        'is_officer': True,
        'officer': Officer.objects.get(user=request.user)
    }
    return render(request, 'officer/detail.html', context)
