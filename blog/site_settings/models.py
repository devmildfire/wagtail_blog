from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

# @register_setting
# class SiteSpecificSocialMediaSettings(BaseSiteSetting):
#     facebook = models.URLField()


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    """Social media settings for a site"""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="twitter URL")
    youtube = models.URLField(blank=True, null=True,
                              help_text="youtube channel")

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("twitter"),
                FieldPanel("youtube"),
            ], heading="Social Media Settings"
        )
    ]
