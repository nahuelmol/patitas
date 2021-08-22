from django.contrib import admin
from db.models import Post, Comment, Event, Dog, Cat

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Dog)
admin.site.register(Cat)
admin.site.register(Event)