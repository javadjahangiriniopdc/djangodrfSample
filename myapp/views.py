from django.shortcuts import render

# Create your views here.
from myapp.models import Profiles
from myapp.serializer import ProfileSerializer
from django.http import JsonResponse


def profile_list(request):
    if request.method == 'GET':
        profiles = Profiles.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return JsonResponse(serializer.data, safe=False)
