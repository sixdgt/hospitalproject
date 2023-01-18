from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hospitalapi.serializers import HospitalSerializer, CategorySerializer
from hospitals.models import Hospital, Category

# Create your views here.
def getSuccessResponse(data, code, msg):
    response_data = {
            'message': msg,
            'status_code': code,
            'data': data,
            'error': [],
            'pagination': [],
        }
    return response_data

def getErrorResponse(error, code, msg):
    response_data = {
            'message': msg,
            'status_code': code,
            'data': [],
            'error': error,
            'pagination': [],
        }
    return response_data

class HospitalApiView(APIView):
    def get(self, request):
        if request.method != "GET":
            msg = 'Method now allow'
            return Response(getErrorResponse(msg, 405, msg))
        data = Hospital.objects.all()
        serializer = HospitalSerializer(data, many=True)
        msg = 'Hospital List'
        return Response(getSuccessResponse(serializer.data, 200, msg), status=status.HTTP_200_OK)

    def post(self, request):
        if request.method == "POST":
            req_data = {
                'full_name': request.POST.get('full_name'),
                'short_name': request.POST.get('short_name'),
                'category': 1,
                'contact': request.POST.get('contact'),
                'address': request.POST.get('address'),
            }
            serializer = HospitalSerializer(data=req_data)
            if serializer.is_valid():
                serializer.save()
                return Response(getSuccessResponse(serializer.data, 201, 'Added success'))
            else:
                return Response(getErrorResponse(serializer.errors, 400, 'Something went wrong'))
        msg = 'Method now allow'
        return Response(getErrorResponse(msg, 405, msg))
