from django.db import models

# Create your models here.
class User(models.Model):
    SEX=(
        ('male','男性'),
        ('female','女性'),
    )
    LOCATION=(
        ('hz', '杭州'),
        ('nb', '宁波'),
        ('wz', '温州'),
        ('jx', '嘉兴'),
    )
    phonenum = models.CharField(max_length=14, unique=True, verbose_name='手机号码')
    nickname = models.CharField(max_length=20, unique=True, verbose_name='昵称')
    sex = models.CharField(max_length=8, choice=SEX, verbose_name='性别')
    birth_year = models.IntegerField(default=2000, verbose_name='出生年份')
    birth_month = models.IntegerField(default=1, verbose_name='出生月份')
    birth_day = models.IntegerField(default=1, verbose_name='出生日期')
    avatar = models.CharField(max_length=256, verbose_name='个人头像')
    location = models.CharField(max_length=8, choices=LOCATION, verbose_name='地址')

    def to_dict(self):
        return {
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'birth_year': self.birth_year,
            'birth_month': self.birth_month,
            'birth_day': self.birth_day,
            'avatar': self.avatar,
            'location': self.location
        }