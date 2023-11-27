from django.shortcuts import render
from .models import UserInfo

def main(request):
    user_info = UserInfo.objects.get(user=request.user)
    return render(request, 'profiles/profile.html', {'user_info': user_info})