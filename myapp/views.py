from django.shortcuts import render

# Create your views here.
from myapp.models import Profiles
from myapp.serializer import ProfileSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def profile_list(request):
    if request.method == 'GET':
        profiles = Profiles.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
