# Generated by Django 4.0.3 on 2022-04-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='tilte',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='page',
            name='datetimecreation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
