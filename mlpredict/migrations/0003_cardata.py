# Generated by Django 4.0.2 on 2022-03-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlpredict', '0002_alter_lifedata_allergies_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_Name', models.CharField(max_length=20)),
                ('Year', models.IntegerField()),
                ('Selling_Price', models.FloatField()),
                ('Present_Price', models.FloatField()),
                ('Kms_Driven', models.IntegerField()),
                ('Fuel_Type', models.IntegerField()),
                ('Seller_Type', models.IntegerField()),
                ('Transmission', models.IntegerField()),
                ('Owner', models.IntegerField()),
            ],
        ),
    ]