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
class branchList(ListView):
    model = Branch
    template_name = 'list_branch.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(branchList, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        query = self.request.GET.get('query')
        if query:
            post_list = Branch.objects.filter(
                Q(branch_name__icontains=query)
            ).order_by('-id')
            context["query"] = query
            context["is_paginated"] = False
        else:
            post_list= Branch.objects.all()
        totalcnt = post_list.count()
        paginator = Paginator(post_list, self.paginate_by)

        try:
            object = paginator.page(page)
        except PageNotAnInteger:
            object = paginator.page(1)
        except EmptyPage:
            object = paginator.page(paginator.num_pages)

        context["post_list"] = object
        context["total_cnt"] = totalcnt

        return context

@login_required
def create(request):
    if request.method=='POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            new_branch = form.save(commit = False)
            new_branch.user = request.user.username
            new_branch.save()
            return redirect('list_branch')
    elif request.method == 'GET':
        form = BranchForm()
    return render(request, 'create_branch.html', {'form':form})

@login_required
def update(request, pk):
    branch = Branch.objects.get(pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST,instance=branch)
        if form.is_valid():
            new_branch = form.save(commit = False)
            new_branch.user = request.user.username
            new_branch.save()
            return redirect('list_branch')
    else:
        form = BranchForm(instance=branch)

    return render(request, 'update_branch.html', {
        'form': form,
    })

@login_required
def delete(request, pk):
    b = get_object_or_404(Branch, pk=pk)
    b.delete()
    return redirect('list_branch')