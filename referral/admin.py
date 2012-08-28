from django.contrib import admin

from models import Campaign, Referrer

class ReferrerInine(admin.TabularInline):
    model = Referrer
    extra = 0

class CampaignAdmin(admin.ModelAdmin):
    inlines = (ReferrerInine, )

class ReferrerAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign', 'creation_date')

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Referrer, ReferrerAdmin)

