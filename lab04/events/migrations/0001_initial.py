# Generated by Django 3.0.4 on 2020-04-28 00:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('babies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=80, null=True)),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('note', models.CharField(max_length=800)),
                ('baby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='babies.Baby')),
            ],
        ),
    ]