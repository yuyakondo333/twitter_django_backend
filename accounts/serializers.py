from rest_framework import serializers
from .models import CustomUser


class CustomDateField(serializers.DateField):
    def to_internal_value(self, data):
        if data == '':
            return None
        return super().to_internal_value(data)


class CustomRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    password_confirmation = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    birthday = CustomDateField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_confirmation', 'birthday']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({
                'non_field_errors': "パスワードが一致しません。"
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        birthday = validated_data.get('birthday', None)
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            birthday=birthday,
        )
        return user
