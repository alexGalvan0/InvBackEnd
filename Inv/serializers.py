from rest_framework import serializers
from .models import Team,Custom_user,ItemType,Item

class Custom_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_user
        fields = ('__all__')

        #hide password from response
        extra_kwargs = {
            'password':{'write_only':True}
        }
        #hash password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ('__all__')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')