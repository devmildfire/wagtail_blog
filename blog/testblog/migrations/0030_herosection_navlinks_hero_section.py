# Generated by Django 4.2.3 on 2023-07-22 06:28

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0029_rename_pp_link_addmebutton_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blackText', models.CharField(max_length=1024)),
                ('blueText', models.CharField(max_length=1024)),
                ('subtext', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='navlinks',
            name='hero_section',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hero_links', to='testblog.herosection'),
        ),
    ]
