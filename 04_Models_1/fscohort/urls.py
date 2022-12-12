

# must be in views.py:
from django.http import HttpResponse
from django.urls import path


def fscohort(request):
    return HttpResponse('''
    <p><b>
        Welcome to FsCohort
    </b></p>
''')

def fscohort2(request):
    return HttpResponse('''
    <p><b>
        Welcome to SubFolder
    </b></p>
''')

urlpatterns = [
    path('', fscohort),
    path('example/', fscohort2),
]