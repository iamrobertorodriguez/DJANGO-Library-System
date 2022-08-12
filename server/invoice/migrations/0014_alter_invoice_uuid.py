# Generated by Django 4.0.6 on 2022-08-11 20:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0013_alter_invoice_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('87877ecf-b4d0-4d7d-8412-0cb774ad8bbc')),
        ),
    ]
