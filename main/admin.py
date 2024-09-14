from django.contrib import admin
from .models import *


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(Upgrade)
class UpgradeAdmin(admin.ModelAdmin):
    pass


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "count", "chance"]


@admin.register(ReferralSystem)
class ReferralSystemAdmin(admin.ModelAdmin):
    pass


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    pass


@admin.register(Skin)
class SkinAdmin(admin.ModelAdmin):
    list_display = ['id', 'league', 'id_prize', 'name', 'description', 'available_skin', 'description',
                    'available_skin', 'is_active', 'skin_type']


# @admin.register(PlayerSkins)
# class PlayerSkinsAdmin(admin.ModelAdmin):
#     list_display = ["id", "prize", "id_prize"]
#
#
# @admin.register(LeagueSkins)
# class LeagueSkinsAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "description", "league", "available_skin", "is_active"]


@admin.register(TaskPlayer)
class TaskPlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "link", "completed", "is_active"]
