from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import DataUser


class UserSerialiser(ModelSerializer):
    class Meta:
        model=DataUser
        fields='__all__'
