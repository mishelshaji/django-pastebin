# Generated by Django 3.1.2 on 2020-10-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200930_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default=None, null=True, upload_to='images', verbose_name='Featured Image'),
        ),
    ]