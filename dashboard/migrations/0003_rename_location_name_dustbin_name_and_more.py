# Generated by Django 5.2.1 on 2025-06-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dustbin',
            old_name='location_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='dustbin',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dustbin',
            name='status',
            field=models.CharField(choices=[('good', 'Good Condition'), ('damaged', 'Damaged'), ('overflowing', 'Overflowing')], default='good', max_length=20),
        ),
        migrations.AlterField(
            model_name='dustbin',
            name='fill_level',
            field=models.IntegerField(default=0, help_text='Fill percentage (0-100)'),
        ),
    ]
