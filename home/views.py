from django.shortcuts import render
from .models import *


def home(request):
    foreword = Foreword.objects.last()
    about_me = AboutMe.objects.last()
    count_up = CountUp.objects.last()
    target = Target.objects.last()
    books = BookSlider.objects.all()[:5]
    activities = CulturalActivity.objects.order_by('-title')
    return render(request, 'home/index.html', {
        'foreword': foreword,
        'about_me': about_me,
        'count_up': count_up,
        'target': target,
        'books': books,
        'activities': activities,
    })

