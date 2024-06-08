from rest_framework import serializers
from booking_app.models import HotelOwner


# class HotelOwnerSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=50)
#     age = serializers.IntegerField()
#     sex = serializers.CharField(max_length=1)
#     owner_exp_status = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return HotelOwner.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.sex = validated_data.get('sex', instance.sex)
#         instance.owner_exp_status = validated_data.get('owner_exp_status', instance.owner_exp_status)
#         instance.save()
#         return instance
class HotelOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelOwner
        fields = ["id", "first_name", "last_name", "sex", "age"]
