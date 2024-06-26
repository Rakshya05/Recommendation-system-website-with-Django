# Generated by Django 5.0 on 2024-03-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('category', models.CharField(choices=[('clothing', 'Clothing'), ('food', 'Food'), ('toys', 'Toys'), ('stationary', 'Stationary')], max_length=20)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='null', upload_to='products')),
                ('keywords', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
