from django import template
from django.utils.html import mark_safe

from ..constants import Status

register = template.Library()


@register.filter
def status_badge(subscriber):
    css_classes = {
        Status.PENDING: 'badge-warning',
        Status.SUBSCRIBED: 'badge-primary',
        Status.UNSUBSCRIBED: 'badge-danger',
        Status.CLEANED: 'badge-secondary',
    }
    badge_class = css_classes[subscriber.status]
    badge_text = subscriber.get_status_display()
    html = f'<span class="badge {badge_class} badge-pill">{badge_text}</span>'
    return mark_safe(html)
