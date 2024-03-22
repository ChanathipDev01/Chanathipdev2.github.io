from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import user, Person, Booking, Room
from django.contrib import messages
# Create your views here.

def home(request):
    name = "admin"
    age = 40
    return render(request, "home.html",{"name":name,"age":age})

# --------------------------- การ search -------------------------------
def search(request):
    room_number = request.GET.get('room_number', None)
    room = None
    if room_number:
        try:
            room = Room.objects.get(room_number=room_number)
        except Room.DoesNotExist:
            room = None
    all_booking = Booking.objects.all()
    if request.method == "POST":
        # รับข้อมูล
        startDate = request.POST["startDate"]
        startTime = request.POST["startTime"]
        endDate = request.POST["endDate"]
        endTime = request.POST["endTime"]
        print(startDate,startTime,endDate,endTime)
        # บันทึกข้อมูล
        booking = Booking.objects.create(
            startDate = startDate,
            startTime = startTime,
            endDate = endDate,
            endTime =  endTime
        )
        booking.save
        messages.success(request,"บันทันวันและเวลาเรียบร้อย")
        return redirect("/search")
    else :
        return render(request, "search.html", {'room': room,"all_booking":all_booking})
    # return render(request,"search.html")

# ------------------------ หน้าหลัก -----------------------------
def index(request):
    all_booking = Booking.objects.all()
    if request.method == "POST":
        # รับข้อมูล
        startDate = request.POST["startDate"]
        startTime = request.POST["startTime"]
        endDate = request.POST["endDate"]
        endTime = request.POST["endTime"]
        print(startDate,startTime,endDate,endTime)
        # บันทึกข้อมูล
        booking = Booking.objects.create(
            startDate = startDate,
            startTime = startTime,
            endDate = endDate,
            endTime =  endTime
        )
        booking.save
        messages.success(request,"บันทันวันและเวลาเรียบร้อย")
        return redirect("/main")
    else :
        return render(request, "index.html",{"all_booking":all_booking})
    
# --------------------- ฟอร์มการกรอกจองห้องเรียน -------------------------
def formroom1(request):
    all_booking = Booking.objects.all()
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        Email = request.POST["Email"]
        detail = request.POST["detail"]
        print(name , Email , detail)
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            Email = Email,
            detail = detail
        )
        person.save
        messages.success(request,"บันทันข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/roomlist")
    else :
        return render(request, "room1.html",{"all_booking":all_booking})

def formroom2(request):
    all_booking = Booking.objects.all()
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        Email = request.POST["Email"]
        detail = request.POST["detail"]
        print(name , Email , detail)
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            Email = Email,
            detail = detail
        )
        person.save
        messages.success(request,"บันทันข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/roomlist")
    else :
        return render(request, "room2.html",{"all_booking":all_booking})

def formroom3(request):
    all_booking = Booking.objects.all()
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        Email = request.POST["Email"]
        detail = request.POST["detail"]
        print(name , Email , detail)
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            Email = Email,
            detail = detail
        )
        person.save
        messages.success(request,"บันทันข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/roomlist")
    else :
        return render(request, "room3.html",{"all_booking":all_booking})

def formroom4(request):
    all_booking = Booking.objects.all()
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        Email = request.POST["Email"]
        detail = request.POST["detail"]
        print(name , Email , detail)
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            Email = Email,
            detail = detail
        )
        person.save
        messages.success(request,"บันทันข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/roomlist")
    else :
        return render(request, "room4.html",{"all_booking":all_booking})

def formroom5(request):
    all_booking = Booking.objects.all()
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        Email = request.POST["Email"]
        detail = request.POST["detail"]
        print(name , Email , detail)
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            Email = Email,
            detail = detail
        )
        person.save
        messages.success(request,"บันทันข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/roomlist")
    else :
        return render(request, "room5.html",{"all_booking":all_booking})

def formroom6(request):
    all_booking = Booking.objects.all()
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        Email = request.POST["Email"]
        detail = request.POST["detail"]
        print(name , Email , detail)
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            Email = Email,
            detail = detail
        )
        person.save
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/roomlist")
    else :
        return render(request, "room6.html",{"all_booking":all_booking})
    
# ------------------------------- แสดงรายการห้อง ------------------------------------
def roomlist(request):
    all_person = Person.objects.all()
    return render(request, "roomlist.html",{"all_person":all_person})

# -------------------------------------- ฟอร์มแก้ไข ------------------------------------
def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.Email = request.POST["Email"]
        person.detail = request.POST["detail"]
        person.save()
        messages.success(request,"อัพเดตข้อมูลเรียบร้อย")
        return redirect("/roomlist")
    else:
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})
    
# --------------------------------------- ฟอร์มการลบ ------------------------------------
def delete (request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/roomlist")

# ---------------------------------------- User ทั่วไป -----------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
        mydata = user.objects.filter(username=username).first()
        print(mydata)
        print(mydata)
        if mydata.password == password :
            # login(request, user)
            return redirect('main')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login.html', {'logout_message': 'You are now logged out.'})  # ส่งข้อความแจ้งเตือนเมื่อ logout สำเร็จ

def booking(request):
    return render(request, 'room1.html')


# def logout_view(request):
#     logout(request)
#     return redirect('/')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         # mydata = user.objects.filter(username=username).values()
#         # print(mydata)
#         # print(mydata)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')  # Assuming you have a dashboard page
#         else:
#             # Handle invalid login
#             return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
#     return render(request, 'login.html')

# def login_user(request):
#     return render(request, "login.html",  )
# def loguot_user(request):
#     pass