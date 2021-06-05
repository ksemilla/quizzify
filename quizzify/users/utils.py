from .models import User

def user_exists(email):
    temp_user = User.objects.filter(email=email).first()
    if temp_user:
        return True
    return False

def get_user_or_none(email):
    return User.objects.filter(email=email).first()