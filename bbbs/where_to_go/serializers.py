from rest_framework import serializers

from .models import Tag, Place


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Tag


class PlaceSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()

    def get_info(self, obj):
        return (f'{obj.get_gender_display()}, '
                f'{obj.age} лет. {obj.get_type_of_rest_display()}')

    class Meta:
        fields = [
            'id',
            'info',
            'chosen',
            'title',
            'address',
            'description',
            'link',
            'image',
            'city',
            'gender',
            'age',
            'type_of_rest',
        ]
        extra_kwargs = {
            'gender': {'write_only': True},
            'age': {'write_only': True},
            'type_of_rest': {'write_only': True},
        }
        model = Place
