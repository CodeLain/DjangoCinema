from django.contrib.auth import authenticate, login


def activate_user(strategy, backend, request, user=None, *args, **kwargs):
    # request = strategy.request
    if user:
        user.is_active = True
        user.save()

    # if backend.name == 'github' and user:
    #     print('enterifsadlfjlsajowen')
    #     print(request)
    #     login(request, user, backend=str(backend))
