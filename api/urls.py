from django.urls import path, include
from api.views import *

urlpatterns = [
    path('blogs/', GetAllBlogsView.as_view(), name='blogs'),
    path('blogs/create/', CreateBlogView.as_view(), name='create-blog'),
    path('blogs/delete/', DeleteBlogView.as_view(), name='delete-blog'),
    path('blogs/update/', UpdateBlogView.as_view(), name='update-blog'),
    path('blogs/<slug>/', GetOneBlogView.as_view(), name='single-blog'),
]
