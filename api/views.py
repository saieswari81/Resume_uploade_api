from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework.views import APIView
# Create your views here.


class ProfileAPIView(APIView):

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'Resume Uploaded Successfully',
                'status': 'Success',
                'candidate': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
