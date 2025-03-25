from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Blog, Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.cache import cache


# Home Page
class HomeView(TemplateView):
    template_name = "main/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context.update({
            'latest_blogs': Blog.objects.order_by('-created_at')[:3],
            'latest_projects': Project.objects.order_by('-created_at')[:3],
            })
       
        return context

# Blog Views
class BlogListView(ListView):
    model = Blog
    template_name = "main/blog_list.html"
    context_object_name = "blogs"
    ordering = ['-created_at']
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog
    template_name = "main/blog_detail.html"

class BlogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Blog
    template_name = "main/blog_form.html"
    fields = ["title", "content", "slug"]
    success_url = reverse_lazy("main:blog_list")

    def test_func(self):
        return self.request.user.is_superuser

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = "main/blog_form.html"
    fields = ["title", "content", "slug"]
    success_url = reverse_lazy("main:blog_list")

    def test_func(self):
        return self.request.user.is_superuser

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = "main/blog_confirm_delete.html"
    success_url = reverse_lazy("main:blog_list")

    def test_func(self):
        return self.request.user.is_superuser

# Project Views
class ProjectListView(ListView):
    model = Project
    template_name = "main/project_list.html"
    context_object_name = "projects"
    ordering = ['-created_at']
    paginate_by = 5

class ProjectDetailView(DetailView):
    model = Project
    template_name = "main/project_detail.html"

class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    template_name = "main/project_form.html"
    fields = ["title", "description", "url"]
    success_url = reverse_lazy("main:project_list")

    def test_func(self):
        return self.request.user.is_superuser

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = "main/project_form.html"
    fields = ["title", "description", "url"]
    success_url = reverse_lazy("main:project_list")

    def test_func(self):
        return self.request.user.is_superuser

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "main/project_confirm_delete.html"
    success_url = reverse_lazy("main:project_list")

    def test_func(self):
        return self.request.user.is_superuser