from faker import Faker
from datetime import date
from django.contrib.auth import get_user_model
from .models import ChucVu, Employess

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
        Phone=fake.phone_number(),
        Address=fake.address(),
        Date_of_birth=fake.date_of_birth(),
        chuc_vu=chuc_vu
    )

    # Tạo bản ghi người dùng và liên kết với bản ghi nhân viên tương ứng
    user = User.objects.create_user(
        email=fake.email(),
        password='password',
        name=fake.name(),
        address=fake.address(),
        isAdmin=fake.boolean()
    )
    employess.user = user
    employess.save()

