from django.db import models
from libs.orm import ModelMixin

# Create your models here.
class User(models.Model, ModelMixin):
    SEX = (
        ('male','男性'),
        ('female','女性'),
    )
    LOCATION = (
        ('hz', '杭州'),
        ('nb', '宁波'),
        ('wz', '温州'),
        ('jx', '嘉兴'),
    )
    phonenum = models.CharField(max_length=14, unique=True, verbose_name='手机号码')
    nickname = models.CharField(max_length=20, unique=True, verbose_name='昵称')
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')
    birth_year = models.IntegerField(default=2000, verbose_name='出生年份')
    birth_month = models.IntegerField(default=1, verbose_name='出生月份')
    birth_day = models.IntegerField(default=1, verbose_name='出生日期')
    avatar = models.CharField(max_length=256, verbose_name='个人头像')
    location = models.CharField(max_length=8, choices=LOCATION, verbose_name='地址')


    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile


class Profile(models.Model, ModelMixin):
    SEX = (
        ('male', '男性'),
        ('female', '女性'),
    )
    LOCATION = (
        ('hz', '杭州'),
        ('nb', '宁波'),
        ('wz', '温州'),
        ('jx', '嘉兴'),
    )
    location = models.CharField(max_length=8, choices=LOCATION, verbose_name='目标地址')
    min_distance = models.IntegerField(default=200, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=500, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=35, verbose_name='最大交友年龄')
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配的性别')
    vibration = models.BooleanField(default=True, verbose_name='开启振动')
    only_matche = models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放')