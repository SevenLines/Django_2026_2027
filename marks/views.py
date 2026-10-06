from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from marks.models import Group


# Create your views here.
class GroupListView(View):
    def get(request, *args, **kwargs):
        groups = list(Group.objects.all().values('id', 'title', 'year'))
        return JsonResponse({
            'data': groups,
        })