# Generated by Django 4.0.3 on 2022-06-06 03:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('matters', '0006_remove_matter_created_by_alter_bank_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('a06cfb8f-c523-414e-a0a1-0814e2ae74bb'), editable=False),
        ),
        migrations.AlterField(
            model_name='conveyancematter',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('b1d8d2e5-f4cb-45a0-9eaf-478b3266e0b3'), editable=False),
        ),
        migrations.AlterField(
            model_name='matter',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('6df7af69-9f4c-4c32-b866-4270d6c17f90'), editable=False),
        ),
    ]
