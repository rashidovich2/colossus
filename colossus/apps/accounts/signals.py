import logging

from django.contrib.auth import (
    user_logged_in, user_logged_out, user_login_failed,
)
from django.dispatch import receiver

from colossus.utils import get_client_ip

logger = logging.getLogger(__name__)


@receiver(user_logged_in)
def log_user_logged_in(sender, request, user, **kwargs):
    ip_address = get_client_ip(request)
    logger.info(f'User "{user}" logged in with IP address "{ip_address}".')


@receiver(user_logged_out)
def log_user_logged_out(sender, request, user, **kwargs):
    ip_address = get_client_ip(request)
    logger.info(f'User "{user}" logged out with IP address "{ip_address}".')


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    ip_address = get_client_ip(request)
    logger.warning(
        f'Log in failed for credentials "{credentials}" with IP address "{ip_address}".'
    )
