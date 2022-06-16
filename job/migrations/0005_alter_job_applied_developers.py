# Generated by Django 4.0.5 on 2022-06-15 14:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0004_merge_20220611_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applied_developers',
            field=models.ManyToManyField(blank=True, null=True, related_name='applied_developers', to=settings.AUTH_USER_MODEL, verbose_name='Applied developers'),
        ),
    ]