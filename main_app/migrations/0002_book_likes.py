# Generated by Django 3.0.7 on 2020-07-13 19:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(related_name='book_post', to=settings.AUTH_USER_MODEL),
        ),
    ]