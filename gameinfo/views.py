from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.db.models import Q
from django.views.generic import ListView
from django.urls import reverse
from .forms import *
from .models import *
import os

class gameinfoList(ListView):
    model = GameInfo
    template_name = 'gameinfo_list.html'
    paginate_by = 20
    page=1

    def get_context_data(self, **kwargs):
        context = super(gameinfoList, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        query = self.request.GET.get('query')

        if query:
            post_list = GameInfo.objects.filter(
                Q(game_name__icontains=query)
            ).order_by('-id')
            context["query"] = query
            context["is_paginated"] = False

        else:
            post_list= GameInfo.objects.all().order_by('-game_id')
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
        context["page"] = page

        return context

def create(request):
    if request.method == 'POST':
        form = GameInfoForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user = request.user.username
            new_form.save()
            return redirect('game_info')
    else:
        form = GameInfoForm()
    return render(request, 'gameinfo_create.html', {'form': form})

def update(request, pk):
    g = GameInfo.objects.get(pk=pk)

    if request.method == 'POST':
        form = GameInfoForm(request.POST,instance=g)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user = request.user.username
            new_form.save()
            return redirect('game_info')
    else:
        form = GameInfoForm(instance=g)

    return render(request, 'gameinfo_update.html', {
        'form': form,
    })

@login_required
def delete(request, pk):
    g = get_object_or_404(GameInfo, pk=pk)
    g.delete()

    return redirect('game_info')

def view_post(request, pk, is_file):
    gameinfo = GameInfo.objects.get(pk=pk)
    movie_list = Movies.objects.all().filter(gameinfo_id=pk).order_by('-id')
    subtitle_list = Subtitle.objects.all().filter(gameinfo_id=pk).order_by('-id')
    image_list = GameImage.objects.all().filter(gameinfo_id=pk,div='image').order_by('-id')
    subimage_list = GameImage.objects.all().filter(gameinfo_id=pk, div='subimage').order_by('-id')
    setting_list = GameImage.objects.all().filter(gameinfo_id=pk,div='setting').order_by('-id')
    faq_list = GameImage.objects.all().filter(gameinfo_id=pk,div='faq').order_by('-id')
    desc_list = GameImage.objects.all().filter(gameinfo_id=pk,div='desc').order_by('-id')
    summary_list = GameImage.objects.all().filter(gameinfo_id=pk,div='summary').order_by('-id')
    moviedetail_list = MovieDetail.objects.all().filter(gameinfo_id=pk).order_by('-id')
    form=''
    moviedetail_results = []
    for movie_detail in moviedetail_list:
        result = {}
        result['pk'] = movie_detail.pk
        result['language_type'] = movie_detail.language_type
        result['cnt_desc'] = movie_detail.cnt_desc
        if Movies.objects.filter(pk=movie_detail.movie_id).exists():
            result['moive_file'] = Movies.objects.filter(pk=movie_detail.movie_id).values_list('file', flat=True)[0]
        subtitle_cnt = Subtitle.objects.filter(pk=movie_detail.subtitle_id).count()
        if subtitle_cnt > 0 :
            result['subtitle_file'] =Subtitle.objects.filter(pk=movie_detail.subtitle_id).values_list('file', flat=True)[0]
        moviedetail_results.append(result)

    if request.method == 'POST':
        if is_file == '1' :
            movie_form = MovieForm(request.POST, request.FILES)
            if movie_form.is_valid():
                movie = movie_form.save(commit=False)
                movie.gameinfo_id = pk
                movie.user = request.user.username
                movie = movie_form.save()
                gameinfo.media_cnt = Movies.objects.filter(gameinfo_id=pk).count()
                gameinfo.save()
                data = {'is_valid': True, 'name': movie.file.name, 'url': movie.file.url}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '2' :
            subtitle_form = SubtitleForm(request.POST, request.FILES)
            if subtitle_form.is_valid():
                subtitle = subtitle_form.save(commit=False)
                subtitle.gameinfo_id = pk
                subtitle.user = request.user.username
                subtitle = subtitle_form.save()
                data = {'is_valid': True, 'name': subtitle.file.name, 'url': subtitle.file.url}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '3' :
            gameimage_form = GameImageForm(request.POST, request.FILES)
            if gameimage_form.is_valid():
                gameimage = gameimage_form.save(commit=False)
                gameimage.gameinfo_id = pk
                gameimage.div = 'image'
                gameimage.user = request.user.username
                gameimage = gameimage_form.save()
                data = {'is_valid': True, 'name': gameimage.file.name, 'url': gameimage.file.url}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '4' :
            gameimage_form = GameImageForm(request.POST, request.FILES)
            if gameimage_form.is_valid():
                gameimage = gameimage_form.save(commit=False)
                gameimage.gameinfo_id = pk
                gameimage.div = 'subimage'
                gameimage.user = request.user.username
                gameimage = gameimage_form.save()
                data = {'is_valid': True, 'name': gameimage.file.name, 'url': gameimage.file.url}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '5' :
            gameimage_form = GameImageForm(request.POST, request.FILES)
            if gameimage_form.is_valid():
                gameimage = gameimage_form.save(commit=False)
                gameimage.gameinfo_id = pk
                gameimage.div = 'setting'
                gameimage.user = request.user.username
                gameimage = gameimage_form.save()
                gameinfo.setting_cnt = GameImage.objects.all().filter(gameinfo_id=pk,div='setting').count()
                gameinfo.save()
                data = {'is_valid': True, 'name': gameimage.file.name, 'url': gameimage.file.url}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '6' :
            gameimage_form = GameImageForm(request.POST, request.FILES)
            if gameimage_form.is_valid():
                gameimage = gameimage_form.save(commit=False)
                gameimage.gameinfo_id = pk
                gameimage.div = 'faq'
                gameimage.user = request.user.username
                gameimage = gameimage_form.save()
                gameinfo.faq_cnt = GameImage.objects.all().filter(gameinfo_id=pk,div='faq').count()
                gameinfo.save()
                data = {'is_valid': True, 'name': gameimage.file.name, 'url': gameimage.file.url}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '7' :
            gameimage_form = GameImageForm(request.POST, request.FILES)
            if gameimage_form.is_valid():
                gameimage = gameimage_form.save(commit=False)
                gameimage.gameinfo_id = pk
                gameimage.div = 'desc'
                gameimage.user = request.user.username
                gameimage = gameimage_form.save()
                gameinfo.desc_cnt = GameImage.objects.all().filter(gameinfo_id=pk,div='desc').count()
                gameinfo.save()
                data = {'is_valid': True, 'name': gameimage.file.name, 'url': gameimage.file.url}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '8' :
            gameimage_form = GameImageForm(request.POST, request.FILES)
            if gameimage_form.is_valid():
                gameimage = gameimage_form.save(commit=False)
                gameimage.gameinfo_id = pk
                gameimage.div = 'summary'
                gameimage.user = request.user.username
                gameimage = gameimage_form.save()
                data = {'is_valid': True, 'name': gameimage.file.name, 'url': gameimage.file.url}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        else:

            form = MovieDetailForm(pk, request.POST)
            if form.is_valid():
                movie_detail = form.save(commit=False)
                movie_detail.gameinfo_id = pk
                movie_detail.user = request.user.username
                movie_detail.save()
                return redirect(reverse('view_post', kwargs={'pk':pk, 'is_file': '0'}))
    else:
        form = MovieDetailForm(pk)

    return render(request, 'view_post.html', {'form': form,'movies': movie_list, "moviedetail_results" : moviedetail_results,'images': image_list,'subimages': subimage_list, 'subtitles': subtitle_list, "settings": setting_list,"faqs": faq_list, "descs":desc_list, "summaries":summary_list,'pk': pk,'is_file': is_file, 'gameinfo_title': gameinfo.game_name})

def view_vod(request, pk):

    movies = get_object_or_404(Movies, pk=pk)
    return render(request, 'view_vod.html', {'movies_file_url': movies.file.url})

import boto
from boto.s3.key import Key
from django.conf import settings

def file_delete(file):
    if settings.DEBUG:
        if os.path.isfile(file.path):
                os.remove(file.path)
    else:
        s3conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID,
                settings.AWS_SECRET_ACCESS_KEY, host=settings.AWS_HOST)
        bucket = s3conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)

        k = Key(bucket)
        id = '/media/%s'%file.name
        k.key = str(id)
        k.delete()

def delete_movie(request, pk):

    movie = get_object_or_404(Movies, pk=pk)
    file_delete(movie.file)
    movie.delete()

    gameinfo_pk = movie.gameinfo_id
    gameinfo = get_object_or_404(GameInfo, pk=gameinfo_pk)
    gameinfo.media_cnt -= 1
    gameinfo.save()
    return redirect(reverse('view_post', kwargs={'pk': gameinfo_pk, 'is_file': '0'}))

def delete_subtitle(request, pk):
    subtitle = get_object_or_404(Subtitle, pk=pk)
    file_delete(subtitle.file)
    subtitle.delete()

    gameinfo_pk = subtitle.gameinfo_id
    return redirect(reverse('view_post', kwargs={'pk':gameinfo_pk, 'is_file': '0'}))

def delete_moviedetail(request, pk):
    moviedetail = get_object_or_404(MovieDetail, pk=pk)
    moviedetail.delete()
    gameinfo_pk = moviedetail.gameinfo_id
    return redirect(reverse('view_post', kwargs={'pk':gameinfo_pk, 'is_file': '0'}))

def delete_image(request, pk):
    game_image = get_object_or_404(GameImage, pk=pk,div='image')
    file_delete(game_image.file)
    game_image.delete()

    gameinfo_pk = game_image.gameinfo_id
    return redirect(reverse('view_post', kwargs={'pk':gameinfo_pk, 'is_file': '0'}))

def delete_setting(request, pk):
    setting = get_object_or_404(GameImage, pk=pk,div='setting')
    file_delete(setting.file)
    setting.delete()

    gameinfo_pk = setting.gameinfo_id
    gameinfo = get_object_or_404(GameInfo, pk=gameinfo_pk)
    gameinfo.setting_cnt -= 1
    gameinfo.save()
    return redirect(reverse('view_post', kwargs={'pk':gameinfo_pk, 'is_file': '0'}))

def delete_faq(request, pk):
    faq = get_object_or_404(GameImage, pk=pk,div='faq')
    file_delete(faq.file)
    faq.delete()

    gameinfo_pk = faq.gameinfo_id
    gameinfo = get_object_or_404(GameInfo, pk=gameinfo_pk)
    gameinfo.faq_cnt -= 1
    gameinfo.save()
    return redirect(reverse('view_post', kwargs={'pk':gameinfo_pk, 'is_file': '0'}))

def delete_desc(request, pk):
    desc = get_object_or_404(GameImage, pk=pk,div='desc')
    file_delete(desc.file)
    desc.delete()

    gameinfo_pk = desc.gameinfo_id
    gameinfo = get_object_or_404(GameInfo, pk=gameinfo_pk)
    gameinfo.desc_cnt -= 1
    gameinfo.save()
    return redirect(reverse('view_post', kwargs={'pk':gameinfo_pk, 'is_file': '0'}))

def delete_summary(request, pk):
    summary = get_object_or_404(GameImage, pk=pk,div='summary')
    file_delete(summary.file)
    summary.delete()

    gameinfo_pk = summary.gameinfo_id
    return redirect(reverse('view_post', kwargs={'pk':gameinfo_pk, 'is_file': '0'}))

def delete_subimage(request, pk):
    subimage = get_object_or_404(GameImage, pk=pk,div='subimage')
    file_delete(subimage.file)
    subimage.delete()

    gameinfo_pk = subimage.gameinfo_id
    return redirect(reverse('view_post', kwargs={'pk':gameinfo_pk, 'is_file': '0'}))

def thema(request, pk, page):
    gameinfo = GameInfo.objects.get(pk=pk)

    try:
        g = GameInfoThema.objects.get(gameinfo=pk)
        if request.method == 'POST':

            form = GameInfoThemaForm(request.POST, instance=g)
            if form.is_valid():
                gamefilter = form.save(commit=False)
                gamefilter.gameinfo_id = pk
                gamefilter.save()
                form.save_m2m()
                return redirect('/gameinfo/?page=%s' % page)
        else:
            form = GameInfoThemaForm(instance=g)

        return render(request, 'view_thema.html', {
            'form': form, 'game_id': gameinfo.game_id, 'gameinfo_title': gameinfo.game_name, 'page':page })

    except:
        if request.method == 'POST':
            form = GameInfoThemaForm(request.POST)
            if form.is_valid():
                gamefilter = form.save(commit=False)
                gamefilter.gameinfo_id = pk
                gamefilter.save()
                form.save_m2m()
                return redirect('/gameinfo/?page=%s' % page)
        else:
            form = GameInfoThemaForm()

        return render(request, 'view_thema.html', {'form': form,  'game_id': gameinfo.game_id, 'gameinfo_title': gameinfo.game_name, 'page':page})


def filters(request,pk,page):
    gameinfo = GameInfo.objects.get(pk=pk)
    g = GameFilter.objects.filter(gameinfo=pk)
    if len(g) > 0:
        if request.method == 'POST':
            form = GameFilterUpdateForm(request.POST, gameinfo_id=pk)
            if form.is_valid():
                GameFilter.objects.filter(gameinfo=pk).delete()
                form.save(gameinfo_id=pk)
                return redirect('/gameinfo/?page=%s' % page)
        else:
            form = GameFilterUpdateForm(gameinfo_id=pk)

        return render(request, 'view_filters.html', {
            'form': form, 'game_id': gameinfo.game_id, 'gameinfo_title': gameinfo.game_name, 'page':page })

    else:
        if request.method == 'POST':
            form = GameFilterCreateForm(request.POST)
            if form.is_valid():
                form.save(gameinfo_id=pk)
                return redirect('/gameinfo/?page=%s' % page)
        else:
            form = GameFilterCreateForm()

        return render(request, 'view_filters.html', {'form': form,  'game_id': gameinfo.game_id, 'gameinfo_title': gameinfo.game_name, 'page':page})