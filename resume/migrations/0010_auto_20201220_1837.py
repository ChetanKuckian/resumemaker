# Generated by Django 3.1.4 on 2020-12-20 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20201220_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workexperiences', to='resume.resume'),
        ),
    ]
