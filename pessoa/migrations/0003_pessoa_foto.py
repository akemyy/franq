# Generated by Django 3.2.6 on 2021-09-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_auto_20210901_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
