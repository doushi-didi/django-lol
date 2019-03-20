from django.utils.deprecation import MiddlewareMixin
from libs.http import render_json
from user.models import User
from common import errors


class AuthMiddleware(MiddlewareMixin):
    AUTH_WHITE_LIST=[
        '/api/user/get_vcode',
        'api/user/check_vcode'
    ]

    def process_request(self, request):
        # 检查当前的URL 是否在白名单上
        if request.path in self.AUTH_WHITE_LIST:
            # URL在白名单内部时直接跳出
            return

        # 检查用户是否登陆
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                return render_json(code=errors.USER_NOT_EXIST)
        else:
            return render_json(code=errors.LOGIN_REIRED)