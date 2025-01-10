from django import forms
from .models import *

class teacher_form(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['userType', 'email', 'fnm', 'dob', 'doj', 'compensation', 'password']

class student_form(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['userType', 'email', 'fnm', 'dob', 'doj', 'rollNumber', 'password']

class teacher_add(forms.ModelForm):
    class Meta:
        model = addteacher
        fields = '__all__'

class student_add(forms.ModelForm):
    class Meta :
        model = addstudent
        fields = '__all__'

class event_form(forms.ModelForm):
    class Meta :
        model = eventbl
        fields = '__all__'

class updateform(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'

class passform(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['password']

class clubform(forms.ModelForm):
    class Meta:
        model = clubtbl
        fields = '__all__'

class bookform(forms.ModelForm):
    class Meta:
        model = Booktbl
        fields = '__all__'