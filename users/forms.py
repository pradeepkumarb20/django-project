from django import forms
from .models import mobiletask,movie,comments
from .models import registermodel
from .validators import validatename,validate_username
from django.forms import ValidationError
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator

class mobileformtask(forms.ModelForm):

    class Meta:
        model = mobiletask
        fields = "__all__"

class moviereviewform(forms.ModelForm):
    class Meta:
        model = movie
        fields = '__all__'
        widgets = {'release_date':forms.DateInput(attrs={'type':'date'}),'blog_date':forms.DateInput(attrs={'type':'date'})}

class commentform(forms.ModelForm):
    class Meta:
        model = comments
        exclude=['comment_date']
        widgets = {'review':forms.HiddenInput}

# class registerform1(forms.ModelForm):
#     class Meta:
#         model=registermodel
#         fields=['first_name','last_name','username','password','phone_no']
#         widgets={'password':forms.PasswordInput}
#         validators=[validatename,validate_username]



class registerform1(forms.ModelForm):
    class Meta:
        model = registermodel
        fields = ['first_name','last_name','username','password','phone_no']
        widgets = {'password':forms.PasswordInput}
        validators=[validatename,validate_username]

class registerform(registerform1):
    validators =[validatename,validate_username]