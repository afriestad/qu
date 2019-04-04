from allauth.socialaccount.models import SocialToken


def allauth_token(user):
    try:
        return SocialToken.objects.get(
            account__user=user,
            account__provider='dataporten',
        ).token
    except SocialToken.DoesNotExist:
        return None
