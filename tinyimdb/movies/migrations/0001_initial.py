# Generated by Django 3.0.8 on 2020-08-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('script', models.TextField()),
                ('actors', models.CharField(max_length=400)),
                ('director', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('budget', models.CharField(max_length=4)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
    ]