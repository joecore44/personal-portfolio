# Generated by Django 4.1 on 2022-08-23 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_client_skill_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]