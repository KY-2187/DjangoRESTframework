from rest_framework import serializers

from .models import Tag, Item


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'


class ItemSerializer(serializers.Serializer):
	text = serializers.CharField(allow_blank=True)
	tag_set = TagSerializer(many=True, read_only=True)


	class Meta:
		model = Item
		fields = ['text', 'tag_set']