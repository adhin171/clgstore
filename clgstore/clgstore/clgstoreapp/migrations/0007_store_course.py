# Generated by Django 4.2.3 on 2023-10-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clgstoreapp', '0006_store_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='course',
            field=models.CharField(blank=True, choices=[], max_length=20),
        ),
    ]
