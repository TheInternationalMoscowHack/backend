# Generated by Django 3.2.4 on 2021-06-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placetype',
            name='place_type_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spot',
            name='address',
            field=models.CharField(default='', max_length=300),
        ),
    ]