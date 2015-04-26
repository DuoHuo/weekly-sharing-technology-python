from rest_framework import serializers
import models

class UserExListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.UserEx


class UserExDetailSerializer(serializers.ModelSerializer):
    card_number = serializers.SerializerMethodField('get_format_number')

    class Meta:
        model = models.UserEx

    def get_format_number(self, obj):
        return '%06d' %obj.id

class UserExLoginSerializer(serializers.ModelSerializer):
#    token = serializer.SerializerMethodField('get_login_token')
    token = serializers.Field(source='token')
    class Meta:
        model = models.UserEx
        
    def get_login_token(self, obj):
        return 
        
        