from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'


def get_vcode(request):
    '''获取验证码'''
    phonenum = request.POST.get('phonemnum')


def check_vcode():
    return None