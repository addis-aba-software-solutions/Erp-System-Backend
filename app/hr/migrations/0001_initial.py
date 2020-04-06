# Generated by Django 3.0.4 on 2020-04-06 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountModel',
            fields=[
                ('accountId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('userName', models.CharField(blank=True, max_length=20, verbose_name='User name')),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CatagoryModel',
            fields=[
                ('subCatagory', models.CharField(auto_created=True, max_length=20)),
                ('catagory', models.CharField(auto_created=True, max_length=20)),
                ('catagoryId', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='claimModel',
            fields=[
                ('levelId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('level', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('companyId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=30, verbose_name='Company name')),
                ('generalManger', models.CharField(max_length=30, verbose_name='General manager')),
                ('contactPerson', models.CharField(max_length=20, verbose_name='Contact person')),
                ('workingField', models.CharField(max_length=20, verbose_name='Working Field')),
                ('paymentOption', models.CharField(max_length=20, verbose_name='Payment option')),
                ('email', models.EmailField(max_length=30)),
                ('tinNumber', models.IntegerField(verbose_name='Tin number')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('departmentId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('departmentName', models.CharField(blank=True, max_length=20, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceModel',
            fields=[
                ('invoiceId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('invoiceNo', models.IntegerField(verbose_name='Invoice number')),
                ('ItemId', models.IntegerField()),
                ('subTotal', models.FloatField(verbose_name='Sub total')),
                ('Total', models.FloatField()),
                ('Tax', models.FloatField()),
                ('retailPrice', models.IntegerField()),
                ('date', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('itemId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('itemName', models.CharField(blank=True, max_length=20)),
                ('quantity', models.IntegerField()),
                ('retailPrice', models.FloatField()),
                ('packaging', models.CharField(max_length=20)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.CatagoryModel', verbose_name='Catagory')),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentModel',
            fields=[
                ('shipmentId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('quantity', models.FloatField()),
                ('receivedStatus', models.CharField(max_length=30, verbose_name='Recieved Status')),
                ('conditionOnTrack', models.CharField(max_length=30, verbose_name='Condition on truack')),
                ('receivedBy', models.CharField(max_length=20, verbose_name='Recieved By')),
                ('dateOnTrack', models.DateField(verbose_name='Date on truck')),
                ('arrivalDate', models.DateField(verbose_name='Arrival date')),
                ('departureDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentStatusModel',
            fields=[
                ('shipmentId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('orderName', models.CharField(max_length=20, verbose_name='Order name')),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='sivModel',
            fields=[
                ('sivId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('sivDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('orderId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('orderName', models.CharField(max_length=20, verbose_name='Order name')),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RoleModel',
            fields=[
                ('roleId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('role', models.CharField(blank=True, max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DepartmentModel', verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('orderId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('orderNumber', models.IntegerField(verbose_name='Order number')),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('orderDate', models.DateField(max_length=20)),
                ('discount', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.ItemModel', verbose_name='Item')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeModel',
            fields=[
                ('employeId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(max_length=15, verbose_name='First name')),
                ('lastName', models.CharField(max_length=15, verbose_name='Last name')),
                ('email', models.CharField(blank=True, max_length=30, unique=True)),
                ('hiredDate', models.DateField(max_length=15, verbose_name='Hired date')),
                ('telephone', models.CharField(max_length=15)),
                ('birthDate', models.DateField(max_length=15, verbose_name='Birth date')),
                ('termOfEmployment', models.DateField(max_length=10, verbose_name='Term of Employment')),
                ('country', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DepartmentModel', verbose_name='Department')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.claimModel', verbose_name='Level')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.RoleModel', verbose_name='Role')),
            ],
        ),
        migrations.AddField(
            model_name='claimmodel',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.RoleModel', verbose_name='Role'),
        ),
    ]