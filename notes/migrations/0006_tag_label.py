# Generated by Django 3.1.7 on 2021-03-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20210323_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='label',
            field=models.CharField(default='null', max_length=30),
            preserve_default=False,
        ),
    ]
