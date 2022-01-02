from django.contrib import admin
from firstapp.models import Topic, WebPage, Record
from firstapp.models import Signed_User

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(Record)
admin.site.register(Signed_User)
