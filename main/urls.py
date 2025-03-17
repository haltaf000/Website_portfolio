from django.urls import path
from . import views

app_name = "main" 

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    # Blogs
    path("blogs/", views.BlogListView.as_view(), name="blog_list"),
    path("blog/new/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog/<slug:slug>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog/<slug:slug>/edit/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<slug:slug>/delete/", views.BlogDeleteView.as_view(), name="blog_delete"),
    # Projects
    path("projects/", views.ProjectListView.as_view(), name="project_list"),
    path("project/new/", views.ProjectCreateView.as_view(), name="project_create"),
    path("project/<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("project/<int:pk>/edit/", views.ProjectUpdateView.as_view(), name="project_update"),
    path("project/<int:pk>/delete/", views.ProjectDeleteView.as_view(), name="project_delete"),
]