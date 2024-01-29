# Generated by Django 3.2.13 on 2023-12-05 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advinterface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CISClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CommunicationClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentAreaClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MathematicsClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SocialSciencesClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cis_classes',
            field=models.ManyToManyField(blank=True, related_name='user_profiles', to='advinterface.CISClass'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='communication_classes',
            field=models.ManyToManyField(blank=True, related_name='user_profiles', to='advinterface.CommunicationClass'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='component_area_classes',
            field=models.ManyToManyField(blank=True, related_name='user_profiles', to='advinterface.ComponentAreaClass'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mathematics_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='advinterface.mathematicsclass'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_sciences_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='advinterface.socialsciencesclass'),
        ),
    ]
