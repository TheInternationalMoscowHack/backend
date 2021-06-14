# Generated by Django 3.2.4 on 2021-06-13 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0002_district_district_id'),
        ('events', '0002_alter_event_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='district',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='districts.district'),
        ),
    ]