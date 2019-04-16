from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from branch.models import *
from .models import *

# Create your views here.

def index(request):
    if request.user.profile.auth == 1:
        branch_list = Branch.objects.all().order_by('-branch_name')
        return render(request, 'togetherMessageLog_index.html', {'branch': branch_list})

class togetherMessageLogList(ListView):
    model = TogeterMessageLog
    template_name = 'togetherMessageLog_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        branch_list = Branch.objects.all().order_by('-branch_name')

        context = super(togetherMessageLogList, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        query = self.request.GET.get('query')
        branch_id = self.kwargs['branch_id']
        branch = Branch.objects.get(pk=branch_id)

        if query:
            post_list = TogeterMessageLog.objects.filter(
                Q(branch_name__icontains=query)
            ).order_by('-id')
            context["query"] = query
            context["is_paginated"] = False
        else:
            post_list= TogeterMessageLog.objects.all().filter(
                Q(sender_branch_id=branch_id) & Q(recv_branch_id=branch_id),
                Q(sender_room_id=999) | Q(recv_room_id=999)).order_by('-id')

        totalcnt = post_list.count()
        paginator = Paginator(post_list, self.paginate_by)

        try:
            object = paginator.page(page)
        except PageNotAnInteger:
            object = paginator.page(1)
        except EmptyPage:
            object = paginator.page(paginator.num_pages)

        context["branch"] = branch_list
        context["branch_id"] = branch_id
        context["branch_name"] = branch.branch_name
        context["post_list"] = object
        context["total_cnt"] = totalcnt

        return context