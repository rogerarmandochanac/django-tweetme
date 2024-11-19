# Generated by Django 4.2.16 on 2024-11-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='create_att',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='description',
        ),
        migrations.AddField(
            model_name='tweet',
            name='content',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
