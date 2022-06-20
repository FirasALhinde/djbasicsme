# Generated by Django 3.2 on 2022-06-20 10:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=' ', upload_to='posts/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
