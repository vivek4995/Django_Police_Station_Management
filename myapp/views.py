from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange
# Create your views here.


# Front Page
def index(request):
    return render(request,'index.html')


# Register Block

def register(request):
    
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'Email already exists'
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['rpassword']:
                otp = randrange(100000,999999)   
                subject = 'AYE VEDHYA, CAPTAIN AMERICA NAHI MILEGI'
                message = '{otp} le color ni maar'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global data 
                data = {
                    'fname' : request.POST['fname'],
                    'lname' : request.POST['lname'],
                    'email' : request.POST['email'],
                    'phone' : request.POST['phone'],
                    'password' : request.POST['password'],
                }

                
                return render(request,'otp.html',{'msg':'OTP sent', 'otp':otp})
            return render(request,'register.html',{'msg':'Both password are not same'})
    return render(request,'register.html')


def otp(request):
    if request.method == 'POST':
        if request.POST['otp']  == request.POST['uotp']:
            global data
            User.objects.create(
                fname = data['fname'],
                lname = data['lname'],
                email = data['email'],
                phone = data['phone'],
                password = data['password'],
            )
            return render(request,'citizen.html',{'msg':'Account Created'})
        return render(request,'otp.html',{'msg':'Invalid OTP', 'otp' : request.POST['otp']})
    return render(request,'citizen.html')

# Login Block

def citizen(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session['email'] = request.POST['email']
                return redirect('home')
            return render(request,'citizen.html',{'msg':'Incorrect Password'})
        except:
            msg = 'E-mail not registered' 
            return render(request,'citizen.html',{'msg':msg})
    return render(request,'citizen.html')


# Citizen Block
def home(request):
    uid = User.objects.get(email=request.session['email']) 
    return render(request,'home.html',{'uid':uid})

def add_FIR(request):
    uid = User.objects.get(email=request.session['email'])
    stationary = Station.objects.all()
    if request.method == 'POST':
        stat = Station.objects.get(id=request.POST['police'])
        if 'evi' and 'ID' in request.FILES:
            FIR.objects.create(
                applicant=uid,
                date=request.POST['date'],
                idate=request.POST['rdate'],
                time=request.POST['time'],
                address=request.POST['address'],
                landmark=request.POST['landmark'],
                charge=request.POST['charge'],
                victim=request.POST['victim'],
                ifname=request.POST['fname'],
                ilname=request.POST['lname'],
                dob=request.POST['dob'],
                iaddress=request.POST['info_address'],
                sfname=request.POST['sname'],
                slname=request.POST['slname'],
                sdetail=request.POST['sdetail'],
                evi=request.FILES['evi'],
                iid=request.FILES['ID'],
                police=stat
            )
        else:
            FIR.objects.create(
                applicant=uid,
                date=request.POST['date'],
                idate=request.POST['rdate'],
                time=request.POST['time'],
                address=request.POST['address'],
                landmark=request.POST['landmark'],
                charge=request.POST['charge'],
                victim=request.POST['victim'],
                ifname=request.POST['fname'],
                ilname=request.POST['lname'],
                dob=request.POST['dob'],
                iaddress=request.POST['info_address'],
                sfname=request.POST['sname'],
                slname=request.POST['slname'],
                sdetail=request.POST['sdetail'],
                police=stat
                )
        msg = 'FIR Added'
        return render(request,'add_FIR.html',{'uid':uid,'stationary':stationary,'msg':msg})
    return render(request,'add_FIR.html',{'uid':uid,'stationary':stationary})

def view_FIR(request):
    uid = User.objects.get(email=request.session['email'])
    FIRs= FIR.objects.filter(applicant=uid)
    return render(request,'view-FIR.html',{'uid':uid,'FIRs':FIRs})

def view_one_FIR(request,pk):
    uid = User.objects.get(email=request.session['email'])
    fir=FIR.objects.get(id=pk)
    return render(request, 'view-one-FIR.html',{'uid':uid,'fir':fir})

def search_station(request):
    uid = User.objects.get(email=request.session['email'])
    stations= Station.objects.all()
    return render(request, 'search_station.html',{'uid':uid,'stations':stations})

def add_com(request):
    uid = User.objects.get(email=request.session['email'])
    stationary = Station.objects.all()
    if request.method == 'POST':
        stat = Station.objects.get(id=request.POST['police'])
        Complaint.objects.create(
            applicant=uid,
            date=request.POST['date'],
            idate=request.POST['rdate'],
            time=request.POST['time'],
            address=request.POST['address'],
            landmark=request.POST['landmark'],
            charge=request.POST['charge'],
            victim=request.POST['victim'],
            ifname=request.POST['fname'],
            ilname=request.POST['lname'],
            dob=request.POST['dob'],
            iaddress=request.POST['info_address'],
            police=stat
        )
        msg = 'Complaint Added'
        return render(request,'add_com.html',{'uid':uid,'stationary':stationary,'msg':msg})
    return render(request,'add_com.html',{'uid':uid,'stationary':stationary})

def view_com(request):
    uid = User.objects.get(email=request.session['email'])
    com= Complaint.objects.filter(applicant=uid)
    return render(request,'view-com.html',{'uid':uid,'com':com})

def view_one_com(request,pk):
    uid = User.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    return render(request, 'view-one-com.html',{'uid':uid,'com':com})

def feedback(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Feedback.objects.create(
            applicant=uid,
            title=request.POST['title'],
            feed=request.POST['feed']
            

        )
        msg='Feedback Sent'
        return render(request,'feedback.html',{'uid':uid, 'msg':msg })
    return render(request,'feedback.html',{'uid':uid})
    




# Header Block

def edit_profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.phone = request.POST['phone']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
    return render(request,'eprofile.html',{'uid':uid})

def view_profile(request):
    uid=User.objects.get(email=request.session['email'])
    return render(request,'view-profile.html',{'uid':uid})

def password(request):
    uid = User.objects.get(email = request.session['email'])
    if request.method == 'POST':
        if request.POST['opassword'] == uid.password:
            if request.POST['password'] == request.POST['rpassword']:
                uid.password = request.POST['password']
                uid.save()
                return render(request,'password.html',{'uid':uid,'msg':'Password has been changed'})
            return render(request,'password.html',{'uid':uid,'msg':'New entered password are different'})
        return render(request,'password.html',{'uid':uid,'msg':'Old Password is incorrect'})
    return render(request,'password.html',{'uid':uid})


def logout(request): 
    del request.session['email']
    return redirect('index')

# Emergency 

def emergency(request):
    return render(request,'emergency.html')

def rules(request):
    return render(request,'rules.html')

def missing(request):
    miss=Missing.objects.all()
    return render(request,'missing.html',{'miss':miss})

def missing_one(request,pk):
    miss=Missing.objects.get(id=pk)
    return render(request, 'missing-one.html',{'miss':miss})


