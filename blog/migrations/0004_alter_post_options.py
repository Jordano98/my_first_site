# Generated by Django 3.2.13 on 2022-06-13 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date']},
        ),
    ]
