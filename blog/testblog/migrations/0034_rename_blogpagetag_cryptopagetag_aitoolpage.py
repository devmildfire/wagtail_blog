# Generated by Django 4.2.3 on 2023-07-24 14:31

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('taggit', '0005_auto_20220424_2025'),
        ('testblog', '0033_blogpage_preview_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPageTag',
            new_name='CryptoPageTag',
        ),
        migrations.CreateModel(
            name='AIToolPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateField(verbose_name='Post date')),
                ('intro', models.CharField(max_length=250)),
                ('body', wagtail.fields.RichTextField(blank=True)),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('tags', modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='testblog.CryptoPageTag', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'AI Tool Page',
                'verbose_name_plural': 'AI Tools Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]