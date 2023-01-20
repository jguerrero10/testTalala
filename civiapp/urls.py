from django.urls import path, include
from rest_framework import routers

from civiapp.views import CitationView, home, create_officer, login_, logout_, update_officer, list_officer, \
    detail_officer, list_citations, detail_citation, delete_officer

router = routers.DefaultRouter()

router.register('citation', CitationView, basename='citation')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),
    path('officer/', list_officer, name='list-officer'),
    path('officer/create/', create_officer, name='create-officer'),
    path('officer/update/<int:id>', update_officer, name='update-officer'),
    path('officer/detail', detail_officer, name='detail-officer'),
    path('officer/delete/<int:id>', delete_officer, name='delete-officer'),
    path('citation/', list_citations, name='list-citation'),
    path('citation/detail/<int:id>', detail_citation, name='detail-citation')
]
