# Generated by Django 3.0.6 on 2020-07-02 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200702_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='void',
            new_name='vote',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='void',
            new_name='vote',
        ),
    ]
