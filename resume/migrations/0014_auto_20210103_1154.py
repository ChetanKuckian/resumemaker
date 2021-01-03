# Generated by Django 3.1.4 on 2021-01-03 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0013_auto_20201225_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='skills',
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='resume.resume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='resume.resume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interest_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
