# Generated by Django 3.2.4 on 2021-07-15 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projectapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeCreateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscribe_project', to='projectapp.projectcreatemodel')),
                ('subscribe_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscribe_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('subscribe_user', 'subscribe_project')},
            },
        ),
    ]
