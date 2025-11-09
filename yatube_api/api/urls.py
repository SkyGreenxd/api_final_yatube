from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register("posts", views.PostViewSet, basename="posts")
router.register(
    r"posts/(?P<post_id>\d+)/comments", views.CommentViewSet, basename="comments"
)
router.register("groups", views.GroupViewSet, basename="groups")
router.register("follow", views.FollowViewSet, basename="follow")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls.jwt")),
]
