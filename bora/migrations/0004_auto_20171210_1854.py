# Generated by Django 2.0 on 2017-12-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bora', '0003_auto_20171210_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]