# Generated by Django 4.2 on 2025-05-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_degree_condition_camp_degree_grade_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='interest',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
