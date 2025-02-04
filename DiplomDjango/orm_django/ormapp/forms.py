from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Логин', required=True)
    password = forms.CharField(min_length=8, label='Пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput)
    firstname = forms.CharField(max_length=30, label='Имя', required=True)
    lastname = forms.CharField(max_length=30, label='Фамилия')
    age = forms.IntegerField(min_value=1, max_value=120, label='Возраст')
