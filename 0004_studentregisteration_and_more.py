# Generated by Django 5.1 on 2024-08-23 09:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_student'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegisteration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Roll_no', models.IntegerField()),
                ('Mobile_No', models.IntegerField()),
                ('Address', models.TextField()),
                ('Pin_code', models.IntegerField()),
                ('Image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='is_available',
            new_name='is_avaliable',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('mens', 'mens'), ('womens', 'womens'), ('kids', 'kids'), ('electronic', 'electronic'), ('special_product', 'special_product')], max_length=50),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
