from django.shortcuts import render
from .forms import *
from django.shortcuts import render,get_object_or_404,redirect
# Create your views here.
from django.views.generic import ListView

def list(request):
 post_list = GameThema.objects.all()
 context = {
     'post_list': post_list,
 }

 return render(request, 'gamethema_list.html', context)

def update(request,pk):
    g = GameThema.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameThemaForm(request.POST,instance=g)
        if form.is_valid():
            gamefilter = form.save(commit=False)
            gamefilter.save()
            form.save()
            return redirect('game_thema')
    else:
        form = GameThemaForm(instance=g)

        return render(request, 'gamethema_update.html', {'form': form})

def create(request):
    if request.method == 'POST':
        form = GameThemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_thema')
    else:
        form = GameThemaForm()

    return render(request, 'gamethema_create.html', { 'form': form})


def delete(request, pk):
    thema_name = get_object_or_404(GameThema, pk=pk)
    thema_name.delete()

    return redirect('thema_name')