from rest_framework import serializers
from .models import Catagerymodule

class CatagerySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Catagerymodule
        fields='__all__'
# class CatagerySerilizer(serializers.Serializer):
#     class Meta:
#         model=Catagerymodule
#         fields='__all__'