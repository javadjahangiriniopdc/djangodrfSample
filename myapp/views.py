from django.shortcuts import render

# Create your views here.
from myapp.models import Profiles
from myapp.serializer import ProfileSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from misc.custom_generic_views import PartialUpdateAPIView


#
# @csrf_exempt
# def profile_list(request):
#     if request.method == 'GET':
#         my_profiles = Profiles.objects.all()
#         my_serializer = ProfileSerializer(my_profiles, many=True)
#         return JsonResponse(my_serializer.data, safe=False)
#
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ProfileSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# class ProfileView(APIView):
#     def get(self, request):
#         my_profiles = Profiles.objects.all()
#         my_serializers = ProfileSerializer(my_profiles, many=True)
#         return Response(my_serializers.data)
#
#     def posts(self):
#         pass

# class ProfileView(generics.ListAPIView):
#     serializer_class = ProfileSerializer
#     queryset = Profiles.objects.all()


# class ProfileView(generics.CreateAPIView):
#     serializer_class = ProfileSerializer
#     queryset = Profiles.objects.all()
#
#
# class ProfileView(generics.ListCreateAPIView):
#     serializer_class = ProfileSerializer
#     queryset = Profiles.objects.all()


# برای لیست کردن و اضافه کردن می توانیم استفاده کنیم حالت ترکیبی get all و create هستش شاید سوال کنید
# چرا بقیه حالت را نمی توانیم بنویسم برای get one و put  و  partial update یا delete
# باید از  retrieveApi باید استفاده کنیم

# class ProfileView(generics.RetrieveAPIView):
#     serializer_class = ProfileSerializer
#     queryset = Profiles.objects.all()

# class ProfileView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProfileSerializer
#     queryset = Profiles.objects.all()

# delete url : http://127.0.0.1:8000/profiles/6

# PATCH http://127.0.0.1:8000/profiles/1
# body --> raw ---> Json(application/json)
# {
# 	    "phone_number": "09148702770"
# }


# PUT http://127.0.0.1:8000/profiles/1
#  {
#        "post":
#            {
#                "title": "new title3",
#                "content": "sample content3"
#            }
#        ,
#    	"phone_number": "09149431772",
#        "first_name": "test3",
#        "last_name": "testfamily3"
#    }


class ProfileRetrieve(PartialUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profiles.objects.all()
