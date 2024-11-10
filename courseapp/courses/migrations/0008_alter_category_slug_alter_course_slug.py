# Generated by Django 5.1.2 on 2024-11-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_date_alter_course_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]
