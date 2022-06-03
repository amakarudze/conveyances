# Generated by Django 4.0.3 on 2022-06-02 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveyancematter',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='conveyancematter',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='conveyancematter',
            name='matters',
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stages', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='conveyancematter',
            name='matters',
            field=models.ManyToManyField(to='matters.matter'),
        ),
    ]