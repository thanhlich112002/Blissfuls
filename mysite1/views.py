from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, decorators
from .forms import MyAuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.conf import settings
from .models import ChucVu, Employess


from faker import Faker
from datetime import date
from django.contrib.auth import get_user_model
# Create your views here.


def home(request):
    return render(request, 'Home/index.html')


def body(request):
    return render(request, 'Home/body.html')

# class MyLoginView(LoginView):
#     authentication_form = MyAuthenticationForm
#     template_name = 'user/login.html'
#     success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

#     def form_valid(self, form):
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password')
#         user = authenticate(self.request, email=email, password=password)
#         if user is not None:
#             login(self.request, user)
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return super().form_invalid(form)


def dangnhap(request):
    if not request.user.is_authenticated:
        user_name = request.POST.get('user')
        pass_word = request.POST.get('pass')
        my_user = authenticate(email=user_name, password=pass_word)
        if my_user is None:
            return render(request, 'Home/index.html')
        login(request, my_user)
        return render(request, 'Home/main.html', {'user': my_user})
    return render(request, 'Home/main.html', {'user': request.user})


def my_logout(request):
    logout(request)
    return render(request, 'Home/index.html')


@decorators.login_required(login_url='Home/index.html')
def main(request):
    return render(request, 'Home/main.html')


def detailUser(request, id):
    nhanvien = Employess.objects.get(user_id=id)
    return render(request, 'Home/NhanVien.html', {'nv': nhanvien})
# Create your views here.


def detailUser_id(request, id):
    nhanvien = Employess.objects.get(pk=id)
    return render(request, 'Home/NhanVien.html', {'nv': nhanvien})


def load_DSNV(request, id):
    nhanvien = Employess.objects.all()
    return render(request, 'Home/danhsachnv.html', {'dsnv': nhanvien, 'id': id})


def dsnv_name(request, id):
    nhanviens = Employess.objects.filter(
        Last_name__contains=request.POST.get('modal-quatity'))
    if nhanviens.count() == 0:
        nhanvien = Employess.objects.all()
        return render(request, 'Home/danhsachnv.html', {'dsnv': nhanvien, 'id': id})
    return render(request, 'Home/danhsachnv.html', {'dsnv': nhanviens, 'id': id})


def add_nv(request):

    return render(request, 'Home/ThemNhanVien.html')


def themnhanvien(request):

    if request.method == 'POST':
        first_name = request.POST.get('First name')
        last_name = request.POST.get('Last name')
        phone = request.POST.get('Phone')
        Address = request.POST.get('Address')
        date = request.POST.get('date')
        chucvu = request.POST.get('cars')
        employee = Employess(First_name=first_name, Last_name=last_name,
                             Phone=phone, Address=Address, Date_of_birth=date, chuc_vu=ChucVu.objects.get(id=chucvu))
        employee.save()
        nhanvien = Employess.objects.all()
        return render(request, 'Home/danhsachnv.html', {'dsnv': nhanvien})

    return render(request, 'ThemNhanVien.html')


def update(request, id):

    if request.method == 'POST':
        x = Employess.objects.get(pk=id)
        x.First_name = request.POST.get('Firstname')
        x.Last_name = request.POST.get('Lastname')
        x.Phone = request.POST.get('Phone')
        x.Address = request.POST.get('Address')
        x.Date_of_birth = request.POST.get('datetime-local')
        x.chuc_vu = ChucVu.objects.get(id=request.POST.get('cars'))
        # employee = Employess(First_name=first_name, Last_name=last_name,
        #                      Phone=phone, Address=Address, Date_of_birth=date, chuc_vu=ChucVu.objects.get(id=chucvu))
        x.save()
        nhanvien = Employess.objects.all()
        return render(request, 'Home/danhsachnv.html', {'dsnv': nhanvien})

    return render(request, 'ThemNhanVien.html')


def delete(request, id):
    nhanvien_de = Employess.objects.get(pk=id)
    nhanvien_de.delete()
    nhanvien = Employess.objects.all()
    return render(request, 'Home/danhsachnv.html', {'dsnv': nhanvien})


def database():
    User = get_user_model()
    fake = Faker('vi_VN')
    chuc_vu1 = ChucVu.objects.create(Name='Quản lý')
    chuc_vu2 = ChucVu.objects.create(Name='Nhân viên')
    chuc_vu3 = ChucVu.objects.create(Name='Bảo vệ')
    chuc_vu1.save()
    chuc_vu2.save()
    chuc_vu3.save()
    for _ in range(10):
        # Tạo bản ghi chức vụ

        # Tạo bản ghi nhân viên
        employess = Employess.objects.create(
            First_name=fake.first_name(),
            Last_name=fake.last_name(),
            Phone=123456789,
            Address=fake.address(),
            Date_of_birth=fake.date_of_birth(),
            chuc_vu=chuc_vu1
        )

        # Tạo bản ghi người dùng và liên kết với bản ghi nhân viên tương ứng
        user = User.objects.create_user(
            email=fake.email(),
            password='123456',
            name=fake.name(),
            address=fake.address(),
            isAdmin=fake.boolean()
        )
        employess.user = user
        employess.save()
    for _ in range(10):
        # Tạo bản ghi chức vụ

        # Tạo bản ghi nhân viên
        employess = Employess.objects.create(
            First_name=fake.first_name(),
            Last_name=fake.last_name(),
            Phone=123456789,
            Address=fake.address(),
            Date_of_birth=fake.date_of_birth(),
            chuc_vu=chuc_vu2
        )

        # Tạo bản ghi người dùng và liên kết với bản ghi nhân viên tương ứng
        user = User.objects.create_user(
            email=fake.email(),
            password='123456',
            name=fake.name(),
            address=fake.address(),
            isAdmin=fake.boolean()
        )
        employess.user = user
        employess.save()
    for _ in range(10):
        # Tạo bản ghi chức vụ

        # Tạo bản ghi nhân viên
        employess = Employess.objects.create(
            First_name=fake.first_name(),
            Last_name=fake.last_name(),
            Phone=123456789,
            Address=fake.address(),
            Date_of_birth=fake.date_of_birth(),
            chuc_vu=chuc_vu3
        )

        # Tạo bản ghi người dùng và liên kết với bản ghi nhân viên tương ứng
        user = User.objects.create_user(
            email=fake.email(),
            password='123456',
            name=fake.name(),
            address=fake.address(),
            isAdmin=fake.boolean()
        )
        employess.user = user
        employess.save()
