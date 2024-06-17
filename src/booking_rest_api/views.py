from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from booking_app.models import HotelOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import HotelOwnerSerializer
from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class HotelOwnerList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HotelOwner.objects.all()
    serializer_class = HotelOwnerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_fields = ["id", "first_name", "last_name", "sex", "age"]
    search_fields = ["id", "first_name", "last_name", "sex", "age"]

    # def get(self, request):
    #     owners = HotelOwner.objects.all()
    #     serializer = HotelOwnerSerializer(owners, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = HotelOwnerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelOwnerDetail(APIView):
    permission_classes = [AllowAny]
    queryset = HotelOwner.objects.all()
    serializer_class = HotelOwnerSerializer
#     def get_object(self, pk):
#         try:
#             return HotelOwner.objects.get(pk=pk)
#         except HotelOwner.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         owner = self.get_object(pk)
#         serializer = HotelOwnerSerializer(owner)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         owner = self.get_object(pk)
#         serializer = HotelOwnerSerializer(owner, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         owner = self.get_object(pk)
#         owner.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
