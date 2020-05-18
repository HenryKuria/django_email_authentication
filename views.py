from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html', context={})

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)

        return redirect('/admin')


