# Generated by Django 4.2.3 on 2023-07-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0041_youraddhere'),
    ]

    operations = [
        migrations.AddField(
            model_name='youraddhere',
            name='link_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]