# Generated by Django 3.0.5 on 2020-04-10 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
        ('manage_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='claim',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Claim', to='hr.claimModel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Department', to='hr.DepartmentModel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employe',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employe', to='hr.EmployeModel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Role', to='hr.RoleModel'),
        ),
    ]
