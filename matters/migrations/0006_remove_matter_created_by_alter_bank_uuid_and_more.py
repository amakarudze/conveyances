# Generated by Django 4.0.3 on 2022-06-06 03:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("matters", "0005_alter_bank_uuid_alter_conveyancematter_uuid_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="matter",
            name="created_by",
        ),
        migrations.AlterField(
            model_name="bank",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.UUID("5c878fde-8db1-4704-ae49-f7787df20a50"),
                editable=False,
            ),
        ),
        migrations.AlterField(
            model_name="conveyancematter",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.UUID("c8bdede7-a7b1-437b-b69c-d8b3ae8fb0e0"),
                editable=False,
            ),
        ),
        migrations.AlterField(
            model_name="matter",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.UUID("0b2523e6-7013-4458-b3c4-6adab369e8b8"),
                editable=False,
            ),
        ),
    ]
