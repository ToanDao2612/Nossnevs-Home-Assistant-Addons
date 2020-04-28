# Generated by Django 3.0.4 on 2020-04-07 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cctv_events', '0002_event_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cctv_events.Event'),
        ),
    ]