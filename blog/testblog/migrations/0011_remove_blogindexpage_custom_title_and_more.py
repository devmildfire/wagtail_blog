# Generated by Django 4.2.3 on 2023-07-08 11:04

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('testblog', '0010_remove_blogpage_tags_delete_blogpagetag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='custom_title',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='blog_image',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='custom_title',
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='testblog.blogpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='testblog.BlogPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
