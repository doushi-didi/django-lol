from django import forms
from user.models import Profile

# 使用forms 来验证models中的每一个字段
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'location', 'min_distance', 'max_distance', 'min_dating_age',
            'max_dating_age', 'dating_sex', 'vibration', 'only_matche',
            'auto_play'
        ]

    def clean_max_distance(self):
        cleaned_data = super().clean()
        if cleaned_data['min_distance'] > cleaned_data['max_distance']:
            raise forms.ValidationError('最小距离 min_distance 不能大于最大距离 max_distance')
        else:
            return cleaned_data['max_distance']


    def clean_max_dating_age(self):
        cleaned_data = super().clean()
        if cleaned_data['min_dating_age'] > cleaned_data['max_dating_age']:
            raise forms.ValidationError('最小交友年龄 min_dating_age 不能大于最大交友年龄 max_dating_age')
        else:
            return cleaned_data['max_dating_age']

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()