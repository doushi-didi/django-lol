from django.apps import AppConfig
from user import logics
from common import errors
from django.core.cache import cache
from common import keys
from user.models import User
from libs.http import render_json
from user.forms import ProfileForm
from user.forms import UploadFileForm


class UserConfig(AppConfig):
    name = 'user'


def get_vcode(request):
    '''获取验证码'''
    phonenum = request.POST.get('phonemnum')
    # 检查手机号是否合法
    if logics.is_phonenum(phonenum):
        # 发送验证码
        logics.sned_vcode(phonenum)
        return render_json()
    else:
        return render_json(code=errors.PHONENUM_ERR)


def check_vcode(request):
    '''检查验证码'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    #检查手机号是否合法
    if logics.is_phonenum(phonenum):
        cached_vcode = cache.get(keys.VCODE_KEY % phonenum)
        if cached_vcode == vcode:
            try:
                user = User.objects.get(phonenum=phonenum)
            except User.DoesNotExist:
                # 如果账号不存在，直接创建账号
                user = User.objects.create(phonenum=phonenum,nickname=phonenum)

            # 在session中记录登陆的状态
            request.session['uuid'] = user.id
            return render_json(data=user.to_dict())
        else:
            return render_json(code=errors.VCODE_ERR)
    else:
        return render_json(code=errors.PHONENUM_ERR)


def get_profile(request):
    '''获取用户个人资料'''
    profile_list = request.user.profile.to_dict()
    return render_json(profile_list)


def set_profile(request):
    '''设置用户的个人信息'''
    form = ProfileForm(request.POST)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.id = request.session['uid']
        profile.save()
        return render_json()
    else:
        return render_json(form.errors, errors.PROFILE_ERR)




