# Generated by Django 4.2.4 on 2023-08-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0050_delete_catalogindexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
