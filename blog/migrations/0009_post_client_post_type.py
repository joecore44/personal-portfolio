# Generated by Django 4.1 on 2022-08-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_skill_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='client',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
