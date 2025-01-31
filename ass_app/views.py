from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from ass_project import settings
# Create your views here.

def index(request):
    user = request.session.get('cuser')
    userType = request.session.get('userType')
    data = eventbl.objects.all()

    tdata = addteacher.objects.count()
    sdata = addstudent.objects.count()
    clubdata = clubtbl.objects.count()
    bookdata = Booktbl.objects.count()
    eventdata = eventbl.objects.count()

    return render(request,'index.html',{'user':user,'userType': userType,'data':data,'bookdata':bookdata,'tdata':tdata,'sdata':sdata,'clubdata':clubdata,'eventdata':eventdata})

def sign_in(request):
    user = request.session.get('cuser')
    global userType
    msg = ""
    if request.method == 'POST':
        userType = request.POST['userType']
        mail = request.POST['email']
        pas = request.POST['password']

        person = signup.objects.filter(email = mail, password = pas, userType = userType)

        if person:
            print("Login sucess...")
            request.session['cuser'] = mail
            request.session['userType'] = userType
            return redirect('/')
        else :
            print("Login umsucess...")
            msg = "Enter currect role, email & password..."
            
    return render(request,'sign_in.html',{'user':user, 'msg':msg})

def sign_up(request):
    user = request.session.get('cuser')
    msg = ""
    if request.method == 'POST':
        userType = request.POST['userType']
        if userType == 'teacher':
            teachreq = teacher_form(request.POST)
            
            if teachreq.is_valid():
                teachreq.save()

                # Email
                sub="TeaStu registration successfully"
                msg=f"Hi !\n\nThank you for registering with TeaStu! We're delighted to have you join us.\n\nIf you need assistance, feel free to contact us at +91 12345 67890 / teastu@gmail.com\nBest regards,\nTeaStu college\n+91 12345 67890 | teastu@gmail.com"
                from_ID=settings.EMAIL_HOST_USER
                to_ID=[request.POST['email']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)

                return redirect('sign_in')
            else :
                print(teachreq.errors)
                msg = "Register unsuccessful"

        elif userType == 'student' :
            studreq = student_form(request.POST)
            if studreq.is_valid():
                studreq.save()

                # Email
                sub="TeaStu registration successfully"
                msg=f"Hi !\n\nThank you for registering with us! We're excited to have you.\n\nNeed help? Contact us anytime at\n\n+91 12345 67890 / teastu@gmail.com\nHappy learning!\n\nBest regards,\nTeaStu college\n+91 12345 67890 | teastu@gmail.com"
                from_ID=settings.EMAIL_HOST_USER
                to_ID=[request.POST['email']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)

                return redirect('sign_in')
            else :
                print(studreq.errors)
                msg = "Register unsuccessful"
    return render(request,'sign_up.html',{'user':user, 'msg':msg})


def loguot(request):
    logout(request)
    return redirect('sign_in')

def staff(request):
    return render(request,'staff.html')

def teachers(request):
    user = request.session.get('cuser')
    T_data = addteacher.objects.all()
    return render(request,'teachers.html',{'T_data':T_data,'user':user})

def add_teacher(request):
    user = request.session.get('cuser')
    msg = ""
    if request.method == 'POST':
        teacherreq = teacher_add(request.POST)
        if teacherreq.is_valid():
            teacherreq.save()
            msg = "Teacher data added..."
        else :
            msg = "Something went wrong..."
    return render(request,'add_teacher.html',{'msg':msg,'user':user})

def student(request):
    user = request.session.get('cuser')
    return render(request,'student.html',{'user':user})

def add_student(request):
    msg = ""
    user = request.session.get('cuser')
    if request.method == 'POST':
        newreq = student_add(request.POST)
        if newreq.is_valid():
            newreq.save()
            msg = "Student added..."
        else:
            newreq.errors()
    return render(request,'add_student.html',{'user':user,'msg':msg})


def delete(request,id):
    T_id = addteacher.objects.get(id=id)
    addteacher.delete(T_id)
    return redirect("teachers")

def delete_acc(request,id):
    T_id = signup.objects.get(id=id)
    signup.delete(T_id)
    print("Delete id sucessfully")
    return redirect("sign_in")

def header(request):
    user = request.session.get('cuser')
    return render(request,'header.html',{'user':user})

def profile(request):
    user = request.session.get('cuser')
    userType = request.session.get('userType')
    data = signup.objects.get(email = user)
    return render(request,'Profile.html',{'user':user,'data':data,'userType':userType})

def emailverify(request):
    if request.method == 'POST':
        cpmail = request.POST['email']
        person = signup.objects.filter(email = cpmail).first()

        if person:
            request.session['cpmail'] = cpmail
            print("Email verified")
            # Email
            sub="Forgot Password"
            msg=f"Hello {person.fnm} !\n\nYou recently requested to reset your password for your TeaStu account. Click the link below to reset it.\n\nhttp://127.0.0.1:8000/resetpass/\nIf you didn’t request this, you can safely ignore this email. Your password won’t change unless you access the link above and create a new one.\nThis link will expire in 24 hours.\nThanks,\nThe TeaStu Team\n+91 12345 67890 | teastu@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub, message=msg, from_email=from_ID, recipient_list=to_ID)
            return redirect('change_pass')
        else :
            print("Email dose not matched")
    return render(request,'emailverify.html')

def change_pass(request):
    if request.method == 'POST':
        newpass = passform(request.POST)
        umail = request.session.get('cpmail')

        cmail = signup.objects.filter(email = umail).first()
        if newpass.is_valid():
            newpass = passform(request.POST,instance=cmail)
            newpass.save()
            print('Sucess...')
            request.session.flush()
            return redirect('sign_in')
        else:
            print(newpass.errors)
    return render(request,'change_pass.html')

def edit_user(request):
    user = request.session.get('cuser')
    cuser = signup.objects.get(email = user)
    if request.method=='POST':
        updateReq = updateform(request.POST,instance=user)
        if updateReq.is_valid():
            updateReq.save()
            
            print("Your profile has been updated!")
            msg="Your profile has been updated!"
            return redirect('Profile')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong...Try again!"
    return render(request,'edit_user.html',{'user':user,'cuser':cuser})

def event(request):
    msg = ""
    user = request.session.get('cuser')
    if request.method == 'POST':
        eventreq = event_form(request.POST, request.FILES)
        if eventreq.is_valid():
            eventreq.save()
            msg = "Event uploaded"
        else:
            print(eventreq.errors)
    return render(request,'event.html',{'user':user,'msg':msg})

def department(request):
    user = request.session.get('cuser')
    return render(request,'department.html',{'user':user})

def campus(request):
    user = request.session.get('cuser')
    return render(request,'campus.html',{'user':user})

def club(request):
    user = request.session.get('cuser')
    data = clubtbl.objects.all()
    userType = request.session.get('userType')
    return render(request,'club.html',{'user':user,'data':data,'userType':userType})

def add_club(request):
    user = request.session.get('cuser')
    msg = ""
    if request.method == 'POST':
        teachreq = clubform(request.POST)
        if teachreq.is_valid():
            teachreq.save()
            return redirect('club')
        else :
            print(teachreq.errors)
            msg = "Register unsuccessful"
    return render(request,'add_club.html',{'user':user,'msg':msg})

def library(request):
    user = request.session.get('cuser')
    bookdata = Booktbl.objects.all()
    userType = request.session.get('userType')
    return render(request,'library.html',{'user':user,'bookdata':bookdata,'userType':userType})

def add_book(request):
    msg = ""
    if request.method == 'POST':
        bookreq = bookform(request.POST,request.FILES)
        if bookreq.is_valid():
            bookreq.save()
            return redirect('library')
        else :
            print(bookreq.errors)
            msg = "Something went wrong"
    return render(request,'add_book.html',{'msg':msg})

def routine(request):
    user = request.session.get('cuser')
    return render(request,'routine.html',{'user':user})
