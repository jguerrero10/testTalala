# Generated by Django 4.1.5 on 2023-01-19 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('civiapp', '0004_remove_citation_vehicle_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clerk',
            name='agency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='clrek_agency', to='civiapp.agency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='officer',
            name='agency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='civiapp.agency'),
            preserve_default=False,
        ),
    ]
