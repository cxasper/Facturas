# Generated by Django 2.1.8 on 2019-05-18 00:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('Invoices', '0002_auto_20190517_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detailinvoice',
            name='invoice_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Invoices.Invoice'),
        ),
        migrations.AddField(
            model_name='detailinvoice',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
