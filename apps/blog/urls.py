from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",views.PostListView.as_view(),name="list"),
    path("post/<slug:slug>/",views.PostDetailView.as_view(),name="detail"),

    # staff dashboard
    path("staff/",views.StaffPostListView.as_view(),name="staff_list"),
    path("staff/create/",views.PostCreateView.as_view(),name="create"),
    path("staff/<slug:slug>/edit/",views.PostUpdateView.as_view(),name="edit"),
    path("staff/<slug:slug>/delete/",views.PostDeleteView.as_view(),name="delete"),
]
