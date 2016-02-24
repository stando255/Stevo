import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings')

import django
django.setup()

from datetime import date

from slango.models import User, Slang, Comments


def populate():
    stevo = add_user('stevo','steviestando@e.mail','dover')
    slang1 = add_slang(stevo,'hankie','shite', 1, date(1,1,1))
    slang2 = add_slang(stevo,'dookie','shite', 2, date(1,1,2))
    slang3 = add_slang(stevo,'turd','shite', 3, date(1,1,3))
    comment = add_comment(stevo,'ridiculous',4,'excellent word','not arsed',date(1,1,1))


def add_user(username, email, password):
    u = User.objects.get_or_create(username=username,email=email,password=password)[0]
    return u

def add_slang(user, word, example, trending_score, date_added):
    s = Slang.objects.get_or_create(user=user,word=word,example=example,trending_score=trending_score,date_added=date_added)[0]
    return s

def add_comment(user,slang,score,comment,definition,date_added):
    c = Comments.objects.get_or_create(user=user,slang=slang,score=score,comment=comment,definition=definition,date_added=date_added)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Slango population script..."
    populate()