# Generated by Django 3.2.4 on 2021-07-19 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecreatemodel',
            name='article_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article_project', to='projectapp.projectcreatemodel'),
        ),
    ]