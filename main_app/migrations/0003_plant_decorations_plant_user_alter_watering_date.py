# Generated by Django 4.2.16 on 2024-09-23 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_decoration_watering'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='decorations',
            field=models.ManyToManyField(to='main_app.decoration'),
        ),
        migrations.AddField(
            model_name='plant',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='watering',
            name='date',
            field=models.DateField(verbose_name='Watering date'),
        ),
    ]
