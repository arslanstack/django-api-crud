from rest_framework.response import Response
from rest_framework import status
from api.models import BlogPost
from rest_framework.views import APIView
from api.serializers import BlogPostSerializer
from api.renderers import BlogPostJSONRenderer
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify


class GetAllBlogsView(APIView):
    renderer_classes = [BlogPostJSONRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBlogView(APIView):
    renderer_classes = [BlogPostJSONRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data.copy()
        title = data.get('title')
        if not title:
            return Response({'error': 'Title is required.'}, status=status.HTTP_400_BAD_REQUEST)
        slug = slugify(title)
        data['slug'] = slug
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetOneBlogView(APIView):
    renderer_classes = [BlogPostJSONRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug, format=None):
        blog = BlogPost.objects.get(slug=slug)
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteBlogView(APIView):
    renderer_classes = [BlogPostJSONRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        blog = BlogPost.objects.get(id=request.data.get('id'))
        blog.delete()
        return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT
                        )


class UpdateBlogView(APIView):
    renderer_classes = [BlogPostJSONRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        blog = BlogPost.objects.get(id=request.data.get('id'))
        data = request.data.copy()
        title = data.get('title')
        if not title:
            return Response({'error': 'Title is required.'}, status=status.HTTP_400_BAD_REQUEST)
        slug = slugify(title)
        data['slug'] = slug
        serializer = BlogPostSerializer(blog, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
