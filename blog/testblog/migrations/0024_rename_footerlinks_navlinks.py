# Generated by Django 4.2.3 on 2023-07-13 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0023_alter_footerlinks_footer_alter_footerlinks_header'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FooterLinks',
            new_name='NavLinks',
        ),
    ]
