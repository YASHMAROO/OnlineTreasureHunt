# Generated by Django 3.0.2 on 2021-02-20 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totallevel', models.IntegerField(default=30)),
                ('numlevel', models.IntegerField(default=30)),
                ('countdown', models.BooleanField(default=False)),
                ('time', models.CharField(default=1, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_number', models.IntegerField()),
                ('image', models.ImageField(default='images/sr1.jpg', upload_to='images')),
                ('display_audio', models.BooleanField(default=False)),
                ('audio', models.FileField(blank=True, default='', upload_to='audio')),
                ('display_video', models.BooleanField(default=False)),
                ('video', models.FileField(blank=True, default='', upload_to='video')),
                ('text', models.TextField()),
                ('hint', models.TextField(default='na')),
                ('answer', models.CharField(max_length=200)),
                ('numuser', models.IntegerField(default=0)),
                ('accuracy', models.FloatField(default=0)),
                ('wrong', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('current_level', models.IntegerField(default=1)),
                ('score', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
