# Generated by Django 3.2 on 2022-01-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220124_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]