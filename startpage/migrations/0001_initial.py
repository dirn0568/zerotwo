# Generated by Django 3.2.4 on 2021-08-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorldcupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_1', models.IntegerField(default=0)),
                ('like_2', models.IntegerField(default=0)),
                ('like_3', models.IntegerField(default=0)),
                ('like_4', models.IntegerField(default=0)),
                ('like_5', models.IntegerField(default=0)),
                ('like_6', models.IntegerField(default=0)),
                ('like_7', models.IntegerField(default=0)),
                ('like_8', models.IntegerField(default=0)),
            ],
        ),
    ]
