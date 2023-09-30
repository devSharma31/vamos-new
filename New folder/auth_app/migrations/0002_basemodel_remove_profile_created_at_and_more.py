# Generated by Django 4.2.5 on 2023-09-17 15:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='profile',
            name='basemodel_ptr',
            field=models.OneToOneField(auto_created=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth_app.basemodel'),
            preserve_default=False,
        ),
    ]
