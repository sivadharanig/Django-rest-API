# Generated by Django 5.1.3 on 2024-11-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagery', '0005_alter_catagerymodule_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagerymodule',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]
