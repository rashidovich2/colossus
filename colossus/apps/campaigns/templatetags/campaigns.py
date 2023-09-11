from django import template
from django.utils.html import mark_safe

from ..constants import CampaignStatus

register = template.Library()


@register.filter
def campaign_status_badge(campaign):
    css_classes = {
        CampaignStatus.SENT: 'badge-primary',
        CampaignStatus.SCHEDULED: 'badge-warning',
        CampaignStatus.DRAFT: 'badge-secondary',
        CampaignStatus.QUEUED: 'badge-dark',
        CampaignStatus.DELIVERING: 'badge-success',
        CampaignStatus.PAUSED: 'badge-warning',
    }
    badge_class = css_classes[campaign.status]
    badge_text = campaign.get_status_display()
    html = f'<span class="badge {badge_class} badge-pill">{badge_text}</span>'
    return mark_safe(html)
