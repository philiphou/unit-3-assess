from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.db.models import Sum

def home(request):
    widgets = Widget.objects.all()
    total_num = Widget.objects.all().aggregate(Sum('quantity'))
    widget_form = WidgetForm()
    return render(request, 'home.html', { 'widgets': widgets, 'total_num': total_num, 'widget_form': widget_form})

def widget_create(request):
    if request.methond=="POST":
        form = WidgetForm
    if form.is_valid():
        form.save()
    return redirect('home')

def widget_delete(request, widgetid):
    Widget.objects.get(id=widgetid).delete()
    return redirect('home')
