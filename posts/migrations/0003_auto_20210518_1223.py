# Generated by Django 3.2.3 on 2021-05-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_photo_img_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='img_url',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='photo',
            name='sharable_link',
            field=models.CharField(default='http://127.0.0.1/photo/lb&!#lmHBvtI', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default=None, max_length=255),
        ),
    ]