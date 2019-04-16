from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from .forms import *
from .models import *
import os
from branch.models import *
from  django.http import HttpResponseRedirect

def index(request):
    if request.user.profile.auth >= 3:
        return redirect(reverse('create_main', kwargs={'branch_id': request.user.profile.branch, 'is_file': '0', 'layer_div': '0'}))
    else:
        branch_list = Branch.objects.all().order_by('-branch_name')
        return render(request, 'main_index.html', {'branch': branch_list})

# Create your views here.
def create(request,branch_id, is_file, layer_div):
    if request.user.profile.auth >= 3:
        branch_list = Branch.objects.all().filter(pk=request.user.profile.branch)
    else:
        branch_list = Branch.objects.all().order_by('-branch_name')

    branch = Branch.objects.get(pk=branch_id)
    guide_list = Guide.objects.all().filter(branch=branch_id).order_by('-id')
    course_list = Course.objects.all().filter(branch=branch_id).order_by('-id')
    layer01 = Layer.objects.filter(branch=branch_id, div=1).last()
    layer01Count = Layer.objects.filter(branch=branch_id, div=1).count()
    layer02 = Layer.objects.filter(branch=branch_id, div=2).last()
    layer02Count = Layer.objects.filter(branch=branch_id, div=2).count()
    layer03 = Layer.objects.filter(branch=branch_id, div=3).last()
    layer03Count = Layer.objects.filter(branch=branch_id, div=3).count()
    layer04 = Layer.objects.filter(branch=branch_id, div=4).last()
    layer04Count = Layer.objects.filter(branch=branch_id, div=4).count()
    layer05 = Layer.objects.filter(branch=branch_id, div=5).last()
    layer05Count = Layer.objects.filter(branch=branch_id, div=5).count()

    if request.method == 'POST':
        if is_file == '1':
            guide_form = GuideForm(request.POST, request.FILES)
            if guide_form.is_valid():
                guide = guide_form.save(commit=False)
                guide.branch_id = branch_id
                guide.user = request.user.username
                guide = guide_form.save()
                data = {'is_valid': True, 'name': guide.file.name, 'url': guide.file.url, 'branch_id': branch_id}
                # return redirect(reverse('create_main', kwargs={'branch_id': branch_id, 'is_file': is_file}))
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '2':
            course_form = CourseForm(request.POST, request.FILES)
            if course_form.is_valid():
                course = course_form.save(commit=False)
                course.branch_id = branch_id
                course.user = request.user.username
                course = course_form.save()
                data = {'is_valid': True, 'name': course.file.name, 'url': course.file.url, 'branch_id': branch_id}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
        elif is_file == '3':
            layer_form = LayerForm(request.POST, request.FILES)
            if layer_form.is_valid():
                layer = layer_form.save(commit=False)
                layer.branch_id = branch_id
                layer.div=layer_div
                layer.type=1
                layer.user = request.user.username
                layer = layer_form.save()
                layer_id = Layer.objects.filter(branch=branch_id, div=layer_div).values('id').last()
                data = {'is_valid': True, 'name': layer.file.name, 'url': layer.file.url, 'branch_id': branch_id,'layer_id': layer_id, 'layer_div': layer_div}
            else:
                data = {'is_valid': False}
            return JsonResponse(data)
    else:
        form = LayerForm()

    return render(request, 'main_create.html', {
        'form': form,
        'branch_id':branch_id,
        'branch_name': branch.branch_name,
        'branch': branch_list,
        'guide': guide_list,
        'course': course_list,
        'layer01': layer01,
        'layer02': layer02,
        'layer03': layer03,
        'layer04': layer04,
        'layer05': layer05,
        'layer01_count': layer01Count,
        'layer02_count': layer02Count,
        'layer03_count': layer03Count,
        'layer04_count': layer04Count,
        'layer05_count': layer05Count,
        'is_file': is_file,

    })

def layersub_create(request,branch_id, layer_id, layer_div):
    if request.user.profile.auth >= 3:
        branch_list = Branch.objects.all().filter(pk=request.user.profile.branch)
    else:
        branch_list = Branch.objects.all().order_by('-branch_name')

    branch = Branch.objects.get(pk=branch_id)
    layerSub = LayerSub.objects.filter(layer=layer_id).order_by('-id')

    if request.method == 'POST':
        layersub_form = LayerSubForm(request.POST, request.FILES)
        if layersub_form.is_valid():
            layersub = layersub_form.save(commit=False)
            layersub.layer_id = layer_id
            layersub.user = request.user.username
            layersub = layersub_form.save()
            data = {'is_valid': True, 'name': layersub.file.name, 'url': layersub.file.url, 'branch_id': branch_id, 'layer_id': layer_id}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
    else:
        form = LayerSubForm()

    return render(request, 'layersub_create.html', {
        'form': form,
        'branch_id':branch_id,
        'branch_name': branch.branch_name,
        'branch': branch_list,
        'layer_id' : layer_id,
        'layer_div': layer_div,
        'layerSub': layerSub,
    })


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

@login_required
def delete_guide(request, pk, branch_id):
    guide = get_object_or_404(Guide, pk=pk)
    file_delete(guide.file)
    guide.delete()

    return redirect(reverse('create_main', kwargs={'branch_id':branch_id, 'is_file': '0', 'layer_div': '0'}))

@login_required
def delete_course(request, pk, branch_id):
    course = get_object_or_404(Course, pk=pk)
    file_delete(course.file)
    course.delete()

    return redirect(reverse('create_main', kwargs={'branch_id':branch_id, 'is_file': '0', 'layer_div': '0'}))

@login_required
def delete_layer(request, pk, branch_id):
    layer = get_object_or_404(Layer, pk=pk)
    file_delete(layer.file)
    layer.delete()
    return redirect(reverse('create_main', kwargs={'branch_id':branch_id, 'is_file': '0', 'layer_div': '0'}))

@login_required
def delete_layersub(request, branch_id, layer_id, layer_div, pk):
    layersub = get_object_or_404(LayerSub, pk=pk)
    file_delete(layersub.file)
    layersub.delete()

    return redirect(reverse('create_layersub', kwargs={'branch_id':branch_id, 'layer_id': layer_id, 'layer_div': layer_div}))