from django.shortcuts import render
from slango.models import User, Slang, Comments

def index(request):
    context_dict = {}
    return render(request, 'slango/index.html', context_dict)

def slango_main(request):

    # create trending and latest lists
    trending_list = Slang.objects.order_by('-trending_score')[:3]
    latest_list=Slang.objects.order_by('-date_added')[:3]

    # add them to context dictionary
    context_dict = {'trending':trending_list, 'latest':latest_list}

    # render them
    return render(request,'slango/slango_main.html', context_dict)