# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=100)),
                ('startTime', models.DateTimeField()),
                ('finishTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LocalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Event')),
                ('group', models.ManyToManyField(to='sitio.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('birth', models.DateTimeField()),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=200)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Gender')),
                ('group', models.ManyToManyField(to='sitio.Group')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='idType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.UserType'),
        ),
        migrations.AddField(
            model_name='user',
            name='profilePic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Picture'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Picture'),
        ),
        migrations.AddField(
            model_name='local',
            name='idType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.LocalType'),
        ),
        migrations.AddField(
            model_name='event',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Local'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='group1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from+', to='sitio.Group'),
        ),
        migrations.AddField(
            model_name='answer',
            name='group2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to='sitio.Group'),
        ),
    ]