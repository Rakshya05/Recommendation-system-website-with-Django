# Generated by Django 5.0 on 2024-03-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0002_rename_produts_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True)),
                ('document_upload', models.FileField(blank=True, upload_to='documents/')),
                ('description', models.TextField()),
            ],
        ),
    ]