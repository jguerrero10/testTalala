import os
import sys

from django.db.models import Q


def main():
    """Run administrative tasks."""
    from django.contrib.auth.models import Group
    from django.contrib.auth.models import Permission

    for group in Group.objects.all():
        if group.name == 'CLERK':
            p = Permission.objects.filter(
                Q(content_type__model='officer')|
                Q(codename='view_citation')
            )
        else:
            p = Permission.objects.filter(
                Q(codename='change_officer') |
                Q(codename='view_officer') |
                Q(codename='view_citation')
            )
        group.permissions.set(p)


if __name__ == '__main__':
    import os
    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'civitecapp.settings')
    django.setup()
    main()
