from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50, label = "Kullanıcı Adı:",required=False)
    password = forms.CharField(max_length = 20, label = "Şifre:", widget = forms.PasswordInput,required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, label = "Kullanıcı Adı:")
    password = forms.CharField(max_length = 20, label = "Şifre:", widget = forms.PasswordInput)
    confirm = forms.CharField(max_length = 20, label = "Şifre doğrula:", widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor")
        
        values = {
            "username":username,
            "password":password,
        }
        return values
