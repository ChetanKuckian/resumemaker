# Generated by Django 3.1.4 on 2020-12-20 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0004_merge_20201220_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cert_user', to='auth.user'),
            preserve_default=False,
        ),
    ]
