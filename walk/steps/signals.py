from django.contrib.auth.models import User
from django.dispatch import receiver

from allauth.account.signals import user_logged_in

from .models import Target


@receiver(user_logged_in)
def user_logged_in_(request, user, **kwargs):
    """
    Create's an instance of target if one does not exist, typically the first time a user log's in
    """
    new_target = User.objects.get(username=user)
    exists = Target.objects.filter(user=user)

    if not exists:
        new_target = Target.objects.create(
            user=user,
            goal=0,
            first_name=user.first_name
            )
        new_target.save()
