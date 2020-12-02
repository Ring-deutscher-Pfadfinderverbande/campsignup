# Generated by Django 3.0.8 on 2020-08-12 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_remove_participant_familymember'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='familyMember',
            field=models.ForeignKey(default=None, help_text='Für die Buchung des Familienpreises muss hier der Name des bereits angemeldeten, den Vollpreis zahlenden Familienmitglieds angegeben werden.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='familyMembers', to='backend.Participant', verbose_name='Name eines weiteren Familienmitglieds'),
        ),
    ]