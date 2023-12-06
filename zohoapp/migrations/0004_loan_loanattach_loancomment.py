# Generated by Django 3.2.20 on 2023-09-21 12:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0003_auto_20230921_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payroll')),
            ],
        ),
        migrations.CreateModel(
            name='LoanAttach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach', models.FileField(blank=True, upload_to='loan_attachments/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payroll')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issue', models.DateField()),
                ('date_expiry', models.DateField()),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_cutting_type', models.CharField(choices=[('percentage', 'Percentage'), ('amount', 'Amount')], default='percentage', max_length=10)),
                ('monthly_cutting_percentage', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('monthly_cutting_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('active', models.BooleanField(default=True)),
                ('payroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payroll')),
            ],
            options={
                'verbose_name_plural': 'Loans',
            },
        ),
    ]
