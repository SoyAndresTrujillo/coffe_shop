# Generated by Django 5.1.2 on 2024-10-25 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, verbose_name='name')),
                ('description', models.TextField(max_length=300, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('available', models.BooleanField(default=True, verbose_name='available')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='image')),
            ],
        ),
    ]
