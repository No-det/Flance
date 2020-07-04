from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import (
    FreelancerSerializer, EmployerSerializer, ProjectSerializer,
    FreelancerProfileSerializer, EmployerProfileSerializer)

@api_view(['POST', 'GET'])
def freelancer_reg(request):
    if request.method == 'POST':
        serializer = FreelancerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = FreelancerSerializer()
    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def employer_reg(request):
    if request.method == 'POST':
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = EmployerSerializer()
    return Response(serializer, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def freelancer_profile(request):
    if request.method == 'POST':
        serializer = FreelancerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.user = request.user
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = FreelancerProfileSerializer()
    return Response(serializer, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def employer_profile(request):
    if request.method == 'POST':
        serializer = EmployerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.user = request.user
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = EmployerProfileSerializer()
    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def project_post(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.creator = request.user
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = ProjectSerializer()
    return Response(serializer, status=status.HTTP_200_OK)


def index(request):
    text = '<br><br><center><h1>FLANCE running</h1></center>'
    return HttpResponse(text)
