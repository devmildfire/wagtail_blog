# Generated by Django 4.2.3 on 2023-07-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0028_rename_link_addmebutton_pp_link_addmebutton_tos_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmebutton',
            old_name='PP_link',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='addmebutton',
            name='ToS_link',
        ),
        migrations.AddField(
            model_name='footer',
            name='PP_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='ToS_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]