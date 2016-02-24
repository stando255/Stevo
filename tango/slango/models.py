from django.db import models
from django.template.defaultfilters import slugify

class User(models.Model):
    username = models.CharField(max_length=128, unique=False)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128, unique=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.username


class Slang(models.Model):
    user = models.ForeignKey(User)
    word = models.CharField(max_length=128,unique=False)
    example = models.CharField(max_length=128,unique=False)
    trending_score=models.IntegerField(default=0)
    date_added=models.DateField()

    def __unicode__(self):
        return self.user + ' ' + self.word

class Comments(models.Model):
    user=models.ForeignKey(User)
    slang=models.CharField(max_length=128,unique=False)
    score=models.IntegerField(default=0)
    comment=models.CharField(max_length=128,unique=False)
    definition=models.CharField(max_length=128,unique=False)
    date_added=models.DateField()

    def __unicode__(self):
        return self.user + ' ' + self.slang + ' ' + str(self.score)