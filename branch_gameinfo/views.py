from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.urls import reverse
from branch.models import *
from .models import *
import json
from django.db import transaction
from django.contrib import messages

def index(request):
    if request.user.profile.auth >= 3:
        return redirect(reverse('branchgame_list', kwargs={'branch_id': request.user.profile.branch}))
    else:
        branch_list = Branch.objects.all().order_by('-branch_name')
        return render(request, 'branchgame_index.html', {'branch': branch_list})

class branchgameList(ListView):
    model = GameInfo
    template_name = 'branchgame_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        if self.request.user.profile.auth >= 3 :
            branch_list = Branch.objects.all().filter(pk=self.request.user.profile.branch)
        else :
            branch_list = Branch.objects.all().order_by('-branch_name')

        context = super(branchgameList, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        query = self.request.GET.get('query')
        branch_id = self.kwargs['branch_id']
        branch = Branch.objects.get(pk=branch_id)

        #table1_cam_list = [c.gameinfo_id for c in BranchGame.objects.filter(branch=branch_id)]
        #post_list = GameInfo.objects.filter(pk__in=table1_cam_list)
        # post_list=  GameInfo.objects.filter(branchgame__gameinfo__isnull=True)
        # post_list =GameInfo.objects.filter(gameinfo_branch__branch=branch_id).order_by('-id')
        # post_list = BranchGame.objects.filter(branch=branch_id).prefetch_related('gameinfo').order_by('-id')
        # post_list = GameInfo.objects.filter(pk__in=table1_cam_list)

        if query:
            query_temp = '%' + query + '%'
            db_query = "SELECT * FROM gameinfo_gameinfo p LEFT OUTER JOIN branch_gameinfo_branchgame t ON " \
                "(p.id=t.gameinfo_id AND t.branch_id=%s) WHERE game_name LIKE %s order by game_id desc"
            post_list = list(GameInfo.objects.raw(db_query, tuple([branch_id, query_temp])))

            context["query"] = query
            context["is_paginated"] = False

        else:
            db_query = "SELECT * FROM gameinfo_gameinfo p LEFT OUTER JOIN branch_gameinfo_branchgame t ON  " \
                           "(p.id=t.gameinfo_id AND t.branch_id=%s) order by game_id desc"
            post_list = list(GameInfo.objects.raw(db_query, [branch_id]))

        total_cnt = BranchGame.objects.filter(branch=branch_id).count()
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
        context["total_cnt"] = total_cnt
        return context

@csrf_exempt
@transaction.atomic
def branchgame_all_insert(request, branch_id):
    if request.user.profile.branch == 9:  # 본사직원
        BranchGame.objects.filter(branch=branch_id).delete()
        gameinfo_list = GameInfo.objects.all()
        for gameinfo in gameinfo_list:
            BranchGame.objects.create(branch_id=branch_id, gameinfo_id=gameinfo.pk,user=request.user.username)

        branch_game_count = BranchGame.objects.filter(branch=branch_id).count()
        Branch.objects.filter(id=branch_id).update(game_cnt=branch_game_count)

        return redirect(reverse('branchgame_list', kwargs={'branch_id': branch_id}))
    else :
        message = "본사에서만 등록가능합니다. 본사에 문의해주세요."
        return HttpResponse(message)

@csrf_exempt
def branchgame_insert(request, branch_id):
    message=""
    location=""

    if request.is_ajax():
        branch_id = Decimal(branch_id)
        selected_leads = request.POST['lead_list_ids']
        unselected_leads = request.POST['unlead_list_ids']
        selected_location = request.POST['location_list_ids']
        selected_cant_explain = request.POST['cant_explain_list_ids']

        selected_leads = json.loads(selected_leads)
        unselected_leads = json.loads(unselected_leads)
        selected_location = json.loads(selected_location)
        selected_cant_explain = json.loads(selected_cant_explain)

        branch_selected_leads = request.POST['branch_lead_list_ids']
        branch_unselected_leads = request.POST['branch_unlead_list_ids']
        branch_selected_location = request.POST['branch_location_list_ids']
        branch_selected_cant_explain = request.POST['branch_cant_explain_list_ids']

        branch_selected_leads = json.loads(branch_selected_leads)
        branch_unselected_leads = json.loads(branch_unselected_leads)
        branch_selected_location = json.loads(branch_selected_location)
        branch_selected_cant_explain = json.loads(branch_selected_cant_explain)

        for i, branch_lead in enumerate(branch_selected_leads):
            if branch_lead != '':
                branch_lead = Decimal(branch_lead)
                if branch_selected_location[i] != '':
                    location = branch_selected_location[i].strip()
                if BranchGame.objects.filter(branch_id=branch_id, gameinfo_id=branch_lead).exists():
                    BranchGame.objects.filter(branch_id=branch_id, gameinfo_id=branch_lead).\
                        update(location=location, is_view=True, cant_explain=branch_selected_cant_explain[i])
                    message = "선택한 게임이 등록되었습니다."
                else:
                    message = "등록된 게임이 없습니다. 본사에 문의해주세요."
            else:
                message = "게임을 선택해주세요."

        for i, branch_lead in enumerate(branch_unselected_leads):
            if branch_lead != '':
                if BranchGame.objects.filter(branch_id=branch_id, gameinfo_id=branch_lead).exists():
                    BranchGame.objects.filter(branch_id=branch_id, gameinfo_id=branch_lead).update(is_view=False)
                    message = "선택한 게임이 등록되었습니다."
              #  else:
            #      message = "본사에서 먼저 게임을 선택해야합니다. 본사에 문의해주세요."

        if request.user.profile.auth <= 2 : #슈퍼어드민 or 본사
            for i, lead in enumerate(selected_leads):
                if lead != '':
                    lead = Decimal(lead)
                    if selected_location[i] != '':
                        location = selected_location[i].strip()
                    if BranchGame.objects.filter(branch_id=branch_id, gameinfo_id=lead).exists():
                        BranchGame.objects.filter(branch_id=branch_id, gameinfo_id=lead).\
                            update(location=location, cant_explain=selected_cant_explain[i])
                    else:
                        BranchGame.objects.create(branch_id=branch_id, gameinfo_id=lead, location=location,
                                                  cant_explain=selected_cant_explain[i],
                                                  user=request.user.username)
                    message = "선택한 게임이 등록되었습니다."
                else:
                    message = "게임을 선택해주세요."

            for i, lead in enumerate(unselected_leads):
                if lead != '':
                    if BranchGame.objects.filter(branch_id=branch_id, gameinfo_id=lead).exists():
                        branchgame = BranchGame.objects.filter(branch_id=branch_id, gameinfo_id=lead).first()
                        BranchGame.objects.filter(pk=branchgame.id).delete()
                        message = "선택한 게임이 등록되었습니다."

            branch_game_count = BranchGame.objects.filter(branch=branch_id).count()
            Branch.objects.filter(id=branch_id).update(game_cnt=branch_game_count)

    return HttpResponse(message)

@csrf_exempt
@transaction.atomic
def branchgame_all_insert(request,branch_id):
    if request.user.profile.branch == 9:  # 본사직원
        BranchGame.objects.filter(branch=branch_id).delete()
        gameinfo_list = GameInfo.objects.all()
        for gameinfo in gameinfo_list:
            BranchGame.objects.create(branch_id=branch_id, gameinfo_id=gameinfo.pk,user=request.user.username)

        branch_game_count = BranchGame.objects.filter(branch=branch_id).count()
        Branch.objects.filter(id=branch_id).update(game_cnt=branch_game_count)

        return redirect(reverse('branchgame_list', kwargs={'branch_id': branch_id}))
    else :
        message = "본사에서만 등록가능합니다. 본사에 문의해주세요."
        return HttpResponse(message)

