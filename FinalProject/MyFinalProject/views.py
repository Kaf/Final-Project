# Create your views here.
from django.forms import ModelForm
from django.http import HttpResponse
from models import *


def home(request):
    return HttpResponse('Welcome To NextGen')
