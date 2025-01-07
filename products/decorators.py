from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def superuser_required(function):
    def check_superuser(user):
        if not user.is_superuser:
            raise PermissionDenied
        return True
    
    decorated_function = user_passes_test(check_superuser)(function)
    return decorated_function