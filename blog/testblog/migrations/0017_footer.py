# Generated by Django 4.2.3 on 2023-07-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0016_delete_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
