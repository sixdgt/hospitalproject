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

class HospitalApiIdView(APIView):
    def get_object(self, id):
        try:
            data = Hospital.objects.get(id=id)
            return data
        except Hospital.DoesNotExist:
            return None
        
    def get(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response(getErrorResponse('No data', 404, 'Data not found'), status=status.HTTP_404_NOT_FOUND)
        serializer = HospitalSerializer(instance)
        return Response(getSuccessResponse(serializer.data, 200, 'Hospital detail'), status=status.HTTP_200_OK)
    
    def put(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response(getErrorResponse('No data', 404, 'Data not found'), status=status.HTTP_404_NOT_FOUND)
        
        req_data = {
            'full_name': request.POST.get('full_name'),
            'short_name': request.POST.get('short_name'),
            'category': 1,
            'contact': request.POST.get('contact'),
            'address': request.POST.get('address'),
        }

        serializer = HospitalSerializer(data=req_data, instance=instance, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(getSuccessResponse(serializer.data, 200, 'Data updated successfully'), status=status.HTTP_200_OK)
        else:
            return Response(getErrorResponse(serializer.errors, 400, 'Something went wrong'), status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        instance_data = self.get_object(id)
        if not instance_data:
            return Response(getErrorResponse('No data', 404, 'Data not found'), status=status.HTTP_404_NOT_FOUND)
        instance_data.delete()
        return Response(getSuccessResponse('Data deleted', 200, 'Data deleted successfully'), status=status.HTTP_200_OK)


