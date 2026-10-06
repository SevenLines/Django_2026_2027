from django.contrib import admin

from marks.models import Discipline, Profile, Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False