from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *


@login_required
def create(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.branch = form.cleaned_data.get('branch')
            user.profile.room_number = form.cleaned_data.get('room_number')
            user.profile.auth = form.cleaned_data.get('auth')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.login_user = request.user.username
            user.save()
        #    messages.success(request, ('계정등록이 완료되었습니다.'))
            return redirect('member_list')
    else:
        form = CreateUserForm()
    return render(request, 'create_member.html', {'form': form})

@login_required
@transaction.atomic
def update(request, id):
    query = request.GET.get('query')
    page = request.GET.get('page')
    u = User.objects.get(pk=id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance=u)
        profile_form = ProfileForm(request.POST, instance=u.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_newform = profile_form.save(commit=False)
            profile_newform.login_user = request.user.username
            profile_newform.save()
         #   messages.success(request, ('Your profile was successfully updated!'))
            return redirect(reverse('member_list') + '?query='+query+'&page='+page )

        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UpdateUserForm(instance = u)
        profile_form = ProfileForm(instance = u.profile)

    return render(request, 'update_member.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'id': id
    })

@login_required
def delete(request,id):
    query = request.GET.get('query')
    page = request.GET.get('page')

    u = get_object_or_404(User, id=id)
    u.delete()

    return redirect('member_list')

def delete2(request,id):
    try:
        u = get_object_or_404(User, id=id)
        u.delete()
        messages.sucess(request, "The user is deleted")

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")
        return render(request, 'member_list.html')

    except Exception as e:
        return render(request, 'member_list.html',{'err':e.message})

class memberList(ListView):

    model = User
    template_name = 'member_list.html'
    paginate_by = 20

    def render_to_response(self, context):

        user_auth = int(self.request.user.profile.auth)
        # General admin의 경우 게임관리로 이동
        if user_auth == 2:
            return redirect('game_info')
        # General Manager의 경우 지점 게임관리로 이동
        elif user_auth == 3:
            return redirect('branchgame_index')
        # buttoner, room의 경우 접근 권한 없음
        elif user_auth > 3:
            return redirect('/accounts/login/')

        page = self.request.GET.get('page', 1)
        branch_id = self.request.GET.get('query')
        branch_list = Branch.objects.order_by('branch_name')

        if branch_id:
            db_query = "select * from auth_user as a, member_profile as b, branch_branch as c " \
                       "where a.id = b.user_id and b.branch = c.id " \
                       "and c.id = %s order by a.username asc"
            post_list = list(User.objects.raw(db_query, [branch_id]))

            context["query"] = int(branch_id)
            context["is_paginated"] = False

        else:
            post_list = list(User.objects.extra(select={'branch_name':'branch_branch.branch_name'},tables=['member_profile','branch_branch'],
                                                   where=['member_profile.user_id=auth_user.id','branch_branch.id=member_profile.branch']).order_by('username'))

        context["page"] = page
        totalcnt = 0
        paginator = Paginator(post_list, self.paginate_by)

        try:
            object = paginator.page(page)
        except PageNotAnInteger:
            object = paginator.page(1)
        except EmptyPage:
            object = paginator.page(paginator.num_pages)

        context["post_list"] = object
        context["total_cnt"] = totalcnt
        context["branch_list"] = branch_list

        return super().render_to_response(context)

def password_reset(request, id):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        page = request.GET.get('page', 1)
        query = request.GET.get('query')

        if password1 != password2 :
            messages.success(request, '비밀번호가 일치하지 않습니다.')
        else:
            if form.is_valid():
                usr = User.objects.get(id=id)
                usr.set_password(password1)
                usr.save()

               # messages.success(request, '비밀번호 변경이 완료되었습니다.')
                return redirect(reverse('member_list') + '?query=' + query + '&page=' + page)
            else:
                messages.error(request, 'Please correct the error below.')
    else:
        form = ResetPasswordForm()
    return render(request, 'password_reset_form.html', {
        'form': form
    })

@login_required
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('list.html')
    else:
        form = CreateUserForm()
    return render(request, 'create_member.html', {'form': form})

