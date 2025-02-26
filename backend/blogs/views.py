from .serializers import BlogsSerializer, AuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blogs, Author

# Create your views here.
class BlogsList(APIView):
    def get(self, request):
        blogs = Blogs.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        print(serializer.data)
        return Response(serializer.data)

class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)