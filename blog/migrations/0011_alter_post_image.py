# Generated by Django 3.2.13 on 2022-06-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/default', upload_to='blog/'),
        ),
    ]
