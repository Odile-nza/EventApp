# Generated by Django 4.0.4 on 2022-04-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_ratedate_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]