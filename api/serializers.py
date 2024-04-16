from rest_framework import serializers
from .models import BlogPost  # Assuming the model name is BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'  # Include all fields from the model
        # OR specify fields explicitly:
        # fields = ('id', 'title', 'slug', 'subtitle', 'content', 'published_date', 'status')
