from rest_framework import serializers
from work.models import Post

class serialset(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'