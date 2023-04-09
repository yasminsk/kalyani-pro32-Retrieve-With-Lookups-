from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
from app.models import *

def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='Cricket')
    #LOW=Webpage.objects.get(topic_name='Cricket')
    LOW=Webpage.objects.exclude(topic_name='Cricket')
    LOW=Webpage.objects.all()[:2:]
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.order_by(Length('name').desc())
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='S')
    LOW=Webpage.objects.filter(name__endswith='l')
    LOW=Webpage.objects.filter(name__contains='u')
    LOW=Webpage.objects.filter(name__in=('Dhoni','Rahul'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{6}')
    LOW=Webpage.objects.filter(Q(topic_name='Kabaddi') & Q(name='Rahul'))
    LOW=Webpage.objects.filter(Q(topic_name='Cricket'))
    
    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2012-07-25')
    LOA=AccessRecord.objects.filter(date__lt='2012-07-25')
    LOA=AccessRecord.objects.filter(date__gte='2012-07-25')
    LOA=AccessRecord.objects.filter(date__lte='2012-07-25')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__year='2012')
    LOA=AccessRecord.objects.filter(date__month='10')
    LOA=AccessRecord.objects.filter(date__day='05')
    LOA=AccessRecord.objects.filter(date__year__gt='2008')
    LOA=AccessRecord.objects.filter(date__month__lt='09')
    LOA=AccessRecord.objects.filter(date__day__gt='16')
    
    d={'access':LOA}
    return render(request,'display_access.html',context=d)
