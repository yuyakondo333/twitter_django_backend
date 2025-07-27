from rest_framework import serializers
from .models import CustomUser
import re

class CustomDateField(serializers.DateField):
    def to_internal_value(self, data):
        if data == '':
            return None
        return super().to_internal_value(data)

class CustomRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    birthday = CustomDateField(required=False,allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'birthday']

    def validate_username(self, value):
        if not re.match(r'^[\w@+.-]+$', value):
            raise serializers.ValidationError({'username': "全角文字は使用できません。"})
    
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'non_field_errors': "パスワードが一致しません。"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        birthday = validated_data.get('birthday', None)
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1'],
            birthday=birthday,
        )
        return user
