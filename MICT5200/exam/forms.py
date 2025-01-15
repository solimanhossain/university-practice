from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class TeacherSalaryForm(forms.Form):
    salary=forms.IntegerField()

class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=['course_name','question_number','total_marks']

class QuestionForm(forms.ModelForm):
    
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),empty_label="Exam Name", to_field_name="id")
    class Meta:
        model=models.Question
        fields=['marks','question','option1','option2','option3','option4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }

class TutorialForm(forms.ModelForm):
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),empty_label="Exam Name", to_field_name="id")

    class Meta:
        model = models.Tutorials
        fields=['marks','question','pdf_file']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model= models.Answer
        fields=['course','pdf_stu']


