# Generated by Django 2.0 on 2017-12-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bora', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
