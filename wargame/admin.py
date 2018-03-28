from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import *


# Use custom login and logout views instead of django admin defaults
def custom_logout(request):
    return redirect(reverse_lazy('logout'))


# TODO: Replace with permissions
admin.site.login = staff_member_required(admin.site.login, login_url=reverse_lazy('login'))
admin.site.logout = custom_logout

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(File)
admin.site.register(Tag)
admin.site.register(Challenge)
admin.site.register(UserChallenge)
admin.site.register(Submission)
