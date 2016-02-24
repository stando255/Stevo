from django.contrib import admin
from slango.models import User, Slang, Comments

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

class SlangAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'definition')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'slang', 'score')

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('username',)}

admin.site.register(User)
admin.site.register(Slang)
admin.site.register(Comments)