# Generated by Django 2.1.8 on 2019-05-17 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('dni', models.CharField(max_length=8)),
                ('phone', models.CharField(max_length=9)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
