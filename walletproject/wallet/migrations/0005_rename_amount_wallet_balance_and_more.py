# Generated by Django 5.1.3 on 2024-11-06 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_remove_wallet_balance'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='amount',
            new_name='balance',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='created_at',
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(choices=[('add', 'Add'), ('remove', 'Remove')], max_length=6)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]