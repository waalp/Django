# Generated by Django 2.1.1 on 2018-09-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180926_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='headimg',
            field=models.ImageField(upload_to='headimg/'),
        ),
    ]