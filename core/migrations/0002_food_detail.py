# Generated by Django 4.1 on 2022-10-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='detail',
            field=models.CharField(default='canadian', max_length=500),
            preserve_default=False,
        ),
    ]
