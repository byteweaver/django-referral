from django.contrib import admin

from .models import Campaign, Referrer, UserReferrer


class ReferrerInine(admin.TabularInline):
    model = Referrer
    extra = 0


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_users')
    inlines = (ReferrerInine, )


class ReferrerAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign', 'creation_date', 'count_users')


class UserReferrerAdmin(admin.ModelAdmin):
    list_display = ('user', 'referrer')
    raw_id_fields = ('user',)


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Referrer, ReferrerAdmin)
admin.site.register(UserReferrer, UserReferrerAdmin)
