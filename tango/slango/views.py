from django.shortcuts import render
from slango.models import User, Slang, Comments

def index(request):
    # generate a user list
    user_list = User.objects.all
    context_dict = {'users':user_list}

    # render page
    return render(request, 'slango/index.html', context_dict)

def slango_main(request,user_name_slug):

    # create trending and latest lists
    trending_list = Slang.objects.order_by('-trending_score')[:3]
    latest_list=Slang.objects.order_by('-date_added')[:3]

    #slugs
    try:
        user = User.objects.get(slug=user_name_slug)

        # add them to context dictionary
        context_dict = {'trending':trending_list, 'latest':latest_list,
                    'user_name':user.username}

    except User.DoesNotExist:
        context_dict = {}


    # render them
    return render(request,'slango/slango_main.html', context_dict)