# Generated by Django 4.2 on 2023-05-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Make', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('Variant', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Displacement', models.IntegerField()),
                ('Cylinder', models.IntegerField()),
                ('Drivetrain', models.CharField(max_length=50)),
                ('Emission', models.CharField(max_length=50)),
                ('Fueltype', models.CharField(max_length=50)),
                ('Bodytype', models.CharField(max_length=50)),
                ('Doors', models.IntegerField()),
                ('Gears', models.IntegerField()),
                ('Seating_capacity', models.IntegerField()),
                ('Type', models.CharField(max_length=50)),
                ('ABS', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=120)),
                ('phone', models.IntegerField()),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust1_name', models.CharField(max_length=100)),
                ('cust1_email', models.EmailField(max_length=120)),
                ('cust1_phone', models.IntegerField(blank=True, null=True)),
                ('car_name', models.CharField(max_length=100)),
                ('choose_date', models.DateField()),
            ],
        ),
    ]