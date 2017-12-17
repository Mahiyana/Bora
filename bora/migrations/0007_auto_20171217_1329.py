# Generated by Django 2.0 on 2017-12-17 13:29

import bora.models
from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bora', '0006_auto_20171212_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='user',
            name='aliik',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=bora.models.aliiki),
        ),
        migrations.AddField(
            model_name='user',
            name='art_name',
            field=models.TextField(null=True, verbose_name='Art name'),
        ),
        migrations.AddField(
            model_name='user',
            name='op_name',
            field=models.TextField(null=True, verbose_name='Operation name'),
        ),
        migrations.AddField(
            model_name='user',
            name='story',
            field=models.TextField(null=True, verbose_name='Story'),
        ),
    ]