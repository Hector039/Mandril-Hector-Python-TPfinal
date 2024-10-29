# Generated by Django 5.1.1 on 2024-10-10 00:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_alter_product_price_alter_product_stock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('userId', models.F('productId'))), name='owner_constraint'), models.UniqueConstraint(fields=('userId', 'productId'), name='unique_product')],
            },
        ),
    ]
