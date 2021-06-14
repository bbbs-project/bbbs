from rest_framework import serializers

from .models import Tag, Question


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Tag


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question
        read_only_fields = ['answer', 'tag']
