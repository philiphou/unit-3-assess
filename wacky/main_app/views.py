from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.db.models import Sum

def home(request):
    widgets = Widget.objects.all()
    sum_value = Widget.objects.all().aggregate(Sum('quantity'))['quantity__sum']
    widget_form = WidgetForm()
    return render(request, 'index.html', { 'widgets': widgets, 'sum_value': sum_value, 'widget_form': widget_form})

def widget_create(request):
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

def widget_delete(request, widgetid):
    Widget.objects.get(id=widgetid).delete()
    return redirect('home')
