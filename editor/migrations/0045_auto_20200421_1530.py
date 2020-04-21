# Generated by Django 2.1.15 on 2020-04-21 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('editor', '0044_remove_editoritem_watching_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='editoritem',
            name='unwatching_users',
            field=models.ManyToManyField(related_name='unwatched_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='unwatching_members',
            field=models.ManyToManyField(related_name='unwatched_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='access',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accesses', to='editor.EditorItem'),
        ),
    ]