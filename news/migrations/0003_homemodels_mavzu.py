# Generated by Django 3.2.8 on 2021-11-23 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_mavzunomi'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemodels',
            name='mavzu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='news.mavzunomi'),
        ),
    ]