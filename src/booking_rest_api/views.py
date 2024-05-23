from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking_app.models import HotelOwner
from .serializers import HotelOwnerSerializer
from django.http import Http404


class HotelOwnerList(APIView):
    def get(self, request):
        owners = HotelOwner.objects.all()
        serializer = HotelOwnerSerializer(owners, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelOwnerDetail(APIView):
    def get_object(self, pk):
        try:
            return HotelOwner.objects.get(pk=pk)
        except HotelOwner.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        owner = self.get_object(pk)
        serializer = HotelOwnerSerializer(owner)
        return Response(serializer.data)

    def put(self, request, pk):
        owner = self.get_object(pk)
        serializer = HotelOwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        owner = self.get_object(pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
