# Generated by Django 4.1.2 on 2023-03-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_alter_contact_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
