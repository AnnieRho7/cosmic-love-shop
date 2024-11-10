# admin.py
from django.contrib import admin
from .models import NewsletterSubscriber


class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    list_filter = ('date_subscribed',)


admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
