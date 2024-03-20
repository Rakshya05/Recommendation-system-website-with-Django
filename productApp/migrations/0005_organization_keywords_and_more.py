# Generated by Django 5.0 on 2024-03-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0004_organization_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='keywords',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='document_upload',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='user_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='keywords',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]