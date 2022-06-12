# Generated by Django 4.0.5 on 2022-06-11 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0002_alter_job_developer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepted_developer', to=settings.AUTH_USER_MODEL, verbose_name='Accepted developer'),
        ),
    ]