"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from review import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create_ticket/', views.createTicket),
    path('create_review/', views.createReview),
    path('create_review_from_ticket/', views.createReviewFromTicket),
    path('subscription/', views.subscription),
    path('display_your_posts/', views.displayYourPosts),
    path('modify_your_review/', views.modifyYourReview),
    path('modify_your_ticket/', views.modifyYourTicket),
    path('', views.flow, name='flux'),
    path('confirmation/', views.confirmation),
    # path('image_upload/', views.book_image_view, name = 'image_upload'),
    # path('success', views.success, name = 'success'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)