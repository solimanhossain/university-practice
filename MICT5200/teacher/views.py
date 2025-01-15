from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from exam import models as QMODEL
from student import models as SMODEL
from exam import forms as QFORM
from simphile import jaccard_similarity
from simphile import compression_similarity
from pdf2image import convert_from_path, convert_from_bytes
from PyPDF2 import PdfReader, PdfFileReader
import pytesseract
import PIL, glob
PIL.Image.MAX_IMAGE_PIXELS = 933120000
import fitz
from cleantext import clean
from gingerit.gingerit import GingerIt
parser = GingerIt()



#for showing signup/login button for teacher
def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'teacher/teacherclick.html')

def teacher_signup_view(request):
    userForm=forms.TeacherUserForm()
    teacherForm=forms.TeacherForm()
    mydict={'userForm':userForm,'teacherForm':teacherForm}
    if request.method=='POST':
        userForm=forms.TeacherUserForm(request.POST)
        teacherForm=forms.TeacherForm(request.POST,request.FILES)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacher=teacherForm.save(commit=False)
            teacher.user=user
            teacher.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('teacherlogin')
    return render(request,'teacher/teachersignup.html',context=mydict)



def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'total_student':SMODEL.Student.objects.all().count()
    }
    return render(request,'teacher/teacher_dashboard.html',context=dict)

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_exam_view(request):
    return render(request,'teacher/teacher_exam.html')


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_exam_view(request):
    courseForm=QFORM.CourseForm()
    if request.method=='POST':
        courseForm=QFORM.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-exam')
    return render(request,'teacher/teacher_add_exam.html',{'courseForm':courseForm})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_exam.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def delete_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher/teacher-view-exam')

@login_required(login_url='adminlogin')
def teacher_question_view(request):
    return render(request,'teacher/teacher_question.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_question_view(request):
    questionForm=QFORM.QuestionForm()
    if request.method=='POST':
        questionForm=QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-question')
    return render(request,'teacher/teacher_add_question.html',{'questionForm':questionForm})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def start_tutorial_view(request):
    tutorialform=QFORM.TutorialForm()
    if request.method=='POST':
        tutorialform=QFORM.TutorialForm(request.POST, request.FILES)
        if tutorialform.is_valid(): 
            tutotial=tutorialform.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            tutotial.course=course     
            tutorialform.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-question')
    return render(request,'teacher/teacher_tutorial_start.html',{"tutorialform" : tutorialform}) 


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_question_view(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_question.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_question_view(request,pk):
    questions=QMODEL.Question.objects.all().filter(course_id=pk)
    tutorials =QMODEL.Tutorials.objects.all().filter(course_id=pk)
    return render(request,'teacher/see_question.html',{'questions':questions, 'tutorials': tutorials})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_question_view(request,pk):
    question=QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_tutorial_view(request,pk):
    tutorial=QMODEL.Tutorials.objects.get(id=pk)
    tutorial.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')



@login_required(login_url='teacherlogin')
def teacher_student_view(request):
    dict={
    'total_student':SMODEL.Student.objects.all().count(),
    }
    return render(request,'exam/admin_student.html',context=dict)

@login_required(login_url='teacherlogin')
def teacher_view_student_view(request):
    students= SMODEL.Student.objects.all()
    return render(request,'teacher/teacher_view_student.html',{'students':students})



@login_required(login_url='adminlogin')
def teacher_view_student_marks_view(request):
    students= SMODEL.Student.objects.all()
    return render(request,'teacher/teacher_view_student_marks.html',{'students':students})

@login_required(login_url='teacherlogin')
def teacher_view_marks_view(request,pk):
    courses = models.Course.objects.all()
    student= SMODEL.Student.objects.get(id=pk)
    # student_id = request.COOKIES.get('student_id')
    # student= SMODEL.Student.objects.get(id=student_id)
    results= models.Result.objects.all().filter(student=student)
    
    response =  render(request,'teacher/teacher_view_marks.html',{'courses':courses, 'results':results})
    response.set_cookie('student_id',str(pk))
    return response

# @login_required(login_url='teacherlogin')
def teacher_check_marks_view(request,pk):

    course = models.Course.objects.get(id=pk)
    student_id = request.COOKIES.get('student_id')
    student= SMODEL.Student.objects.get(id=student_id)

    results= models.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'teacher/teacher_check_marks.html',{'results':results})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_tutorial_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_tutorial.html',{'courses':courses})

# @login_required(login_url='teacherlogin')
# @user_passes_test(is_teacher)  
def pdf_ocr(pdfs):
    pdf_text = ""

    for pdf_path in pdfs:
        pages = convert_from_path(pdf_path, 1500)
        for pageNum,imgBlob in enumerate(pages):
            pdf_text = pytesseract.image_to_string(imgBlob,lang='eng')
            
    return pdf_text


def compare_text(answers,grammer):

    jaccard = float(jaccard_similarity(answers,grammer))
    compression = float(compression_similarity(answers,grammer))

    total_mark = (jaccard+compression)/2
    percent_mark = int(total_mark*100)

    return percent_mark


def grammer_check(answer_texts):
    grammer_chacked = []

    for answer_text in answer_texts:
        answer_text = clean(answer_text,fix_unicode=True,to_ascii=True, no_punct=False,no_emoji=True, lang="en")
        grammer_chacked.append(check_grammer(answer_text))

    return grammer_chacked

def exam_mark_check(request):
    file1  = staticfiles_storage.path('pdf/content1.pdf')
    print(file1)
    # question_text = pdf_ocr(file1)
    # print(f"Question in pdf : \n{file1}\nQuestion Content text is :\n\n\n{question_text}\n")
    # print('\nTesting\n')

    reader = PdfReader(file1)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    answer_texts = page.extract_text()
    # print(text)
    
    # students_mark = []

    # for i in range(len(answer_texts)):
    #     answer_texts[i] = clean(answer_texts[i],fix_unicode=True,to_ascii=True, no_punct=False,no_emoji=True, no_line_breaks=True, lang="en")
    #     mark = compare_text(answer_texts[i],grammer_chacked[i])
    #     students_mark.append(mark)

    mark = compare_text(answer_texts,answer_texts)
    print(f"\n\n{file1} mark is {mark}\n\n")

    return render(request,'teacher/base.html',{'mark':mark,'text':answer_texts})