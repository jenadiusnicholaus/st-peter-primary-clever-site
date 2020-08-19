from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.PostView.as_view(), name='blog'),
    path('about/', views.about, name='about'),
    path('postdetails/<int:pk>', views.PostDetails.as_view(), name='post_details'),
    path('post_comment/<int:pk>', views.post_comment, name='post_comment'),
    path('contact/', views.Contact.as_view(), name='contact'),
]


