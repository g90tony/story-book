# Generated by Django 3.2.3 on 2021-05-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='img_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]