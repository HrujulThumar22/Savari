from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm,widgets
from userAccount.models import User


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        labels={'dob':('D.O.B')}
        fields = ["username", "password1", "password2", "dob", "email", "first_name", "last_name","mobile"]
        widgets={'dob':widgets.DateInput(attrs={'type':'date'})}

class UpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=User
        labels={'dob':('D.O.B')}
        fields = ["username", "dob", "email", "first_name", "last_name","mobile"]
        widgets={'dob':widgets.DateInput(attrs={'type':'date'})}