# Generated by Django 4.2.3 on 2023-07-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0027_remove_addmebutton_url_remove_gotobutton_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmebutton',
            old_name='link',
            new_name='PP_link',
        ),
        migrations.AddField(
            model_name='addmebutton',
            name='ToS_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
