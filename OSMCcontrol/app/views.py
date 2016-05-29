"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import platform
import psutil

def get_human_readable_size(num):
    exp_str = [ (0, 'B'), (10, 'KB'),(20, 'MB'),(30, 'GB'),(40, 'TB'), (50, 'PB'),]
    #exp_str = [ (0, 'B'), (10, 'KB'), (20, 'MB'),]
    i = 0
    while i+1 < len(exp_str) and num >= (2 ** exp_str[i+1][0]):
        i += 1
        rounded_val = round(float(num) / 2 ** exp_str[i][0], 2)
    return '%s %s' % ((rounded_val), exp_str[i][1])

def get_human_readable_percentage(num):
    return '%s %%' % (round(float(num), 2))

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'si_system':platform.system(),
            'si_platform':platform.platform(),
            'si_machine':platform.machine(),
            'si_processor':platform.processor(),
            'si_cpu_load':get_human_readable_percentage(psutil.cpu_percent()),
            'si_memory_total':get_human_readable_size(psutil.virtual_memory().total),
            'si_memory_free':get_human_readable_size(psutil.virtual_memory().free),
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
