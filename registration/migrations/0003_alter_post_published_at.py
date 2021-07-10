# Generated by Django 3.2.5 on 2021-07-10 05:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='投稿日'),
            preserve_default=False,
        ),
    ]
