# Generated by Django 3.2.4 on 2021-06-24 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0009_auto_20210624_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='expense',
        ),
        migrations.AddField(
            model_name='expense',
            name='issuer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='prev_balance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.wallet'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]