# Generated by Django 3.2.5 on 2021-07-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(null=True, verbose_name='投稿日'),
        ),
    ]