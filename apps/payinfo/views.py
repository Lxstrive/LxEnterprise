from django.shortcuts import render


def payinfo(request):
    return render(request, 'payinfo/payinfo.html')


def auth_test(request):
    return render(request, 'common/auth.html')
