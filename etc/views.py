from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.db import transaction
from django.urls import reverse
# Create your views here.

def create(request):
    etc = Etc.objects.get(pk=1)
    if request.method == 'POST':
        form = etcForm(request.POST,instance=etc)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user = request.user.username
            new_form.save()

            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('create_etc')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = etcForm(instance = etc)

    return render(request, 'create_etc.html', {
        'form': form
    })