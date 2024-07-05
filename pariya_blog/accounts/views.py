from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from bloggers.models import BloggerModel
from django.db import transaction
import re
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required



def login(request):
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']
        if re.match(EMAIL_REGEX, username_or_email):
            email = username_or_email
            user = User.objects.get(email=email)
            if not user.check_password(password):
                messages.error(request, 'رمز وارد شده اشتباه است.')
                return redirect('login')
        else:
            username = username_or_email
            user = authenticate(request, username=username, password=password)
           
        if user:
            auth.login(request, user)
            messages.success(request, 'ورود با موفقعیت انجام شد')
            return redirect('index')
        else:
            messages.error(request, 'اطلاعات وارد شده اشتباه است.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')



def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'ایمیل استفاده شده تکراری است')
            return redirect('register')

        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'نام کاربری استفاده شده تکراری است')
            return redirect('register')

        password = request.POST['password']
        password2 = request.POST['password2']
        if len(password) < 8 :
            messages.error(request, 'پسورد باید حداقل ۸ کاراکتر باشد.')
            return redirect('register')

        if password != password2:
            messages.error(request, 'تکرار پسورد اشتباه است')
            return redirect('register')

        if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
            messages.error(request, 'پسورد باید شامل حروف و اعداد باشد.')
            return redirect('register')

        else:
            try:
                with transaction.atomic():
                # create user
                    user = User.objects.create_user(username=username,
                            password=password,
                            email=email,
                            first_name=request.POST.get("first_name", None),
                            last_name=request.POST.get("last_name", None))


                    # make user staff
                    user.is_staff = True
                    user.save()

                    # create blogger
                    blogger = BloggerModel.objects.create(
                            user=user,
                            name=request.POST.get("first_name", None),
                            email =email)
                            

                    # Add user to Users group
                    users_group, created = Group.objects.get_or_create(name='Users')
                    user.groups.add(users_group)

                    # login created user
                    messages.success(request, 'ثبت نام با موفقیت انجام شد.')
                    auth.login(request, user)
                    return redirect('index')

            except Exception as e:
                messages.error(request, 'مشکلی در ثبت اطلاعات رخ داده . دوباره تلاش کنید!.')
                return redirect('register')

    else:
        return render(request, 'accounts/register.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'خروج با با موفقیت انجام شد.')
    return redirect('index')