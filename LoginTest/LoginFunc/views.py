from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from LoginFunc import models

# Create your views here.

# 验证登陆
@csrf_exempt
def login(request):
    log_status = 'All blanks should be WRITTEN!'

    if request.method == "POST":
        input_usr = request.POST['username']
        input_pwd = request.POST['pwd']

        if input_usr and input_pwd:
            try:
                usr = models.UserInfo.objects.get(username=input_usr)
                if usr.pwd == input_pwd:
                    return redirect('https://www.baidu.com')
                else:
                    log_status = 'ERROR! Incorrect password!'
            except:
                log_status = 'ERROR! Username does not exist!'
        else:
            log_status = 'ERROR! Username or password cannot be empty!'

    user_list = models.UserInfo.objects.all()
    return render(request, 'login.html', {'data': user_list, 'status': log_status})

# 注册账户
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        # 将用户信息添加到数据库
        models.UserInfo.objects.create(username=username, pwd=pwd)

    user_list = models.UserInfo.objects.all()
    return render(request, 'signup.html', {'data':user_list})
