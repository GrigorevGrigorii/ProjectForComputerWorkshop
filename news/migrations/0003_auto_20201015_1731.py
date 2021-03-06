# Generated by Django 3.1.1 on 2020-10-15 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='username',
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.CharField(max_length=256),
        ),
    ]
