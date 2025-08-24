from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from .mixins import StaffRequiredMixin


class PostListView(ListView):
    queryset           = Post.objects.filter(status=Post.PUBLISHED)
    template_name      = "blog/list.html"
    paginate_by        = 6
    context_object_name = "posts"


class PostDetailView(DetailView):
    model         = Post
    template_name = "blog/detail.html"
    slug_field    = "slug"


class StaffPostListView(StaffRequiredMixin, ListView):
    template_name = "blog/staff_list.html"
    model         = Post
    paginate_by   = 10
    ordering      = ["-created_at"]


class PostCreateView(StaffRequiredMixin, CreateView):
    form_class    = PostForm
    template_name = "blog/form.html"
    success_url   = reverse_lazy("blog:staff_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created.")
        return super().form_valid(form)


class PostUpdateView(StaffRequiredMixin, UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = "blog/form.html"
    slug_field    = "slug"

    def form_valid(self, form):
        messages.success(self.request, "Post updated.")
        return super().form_valid(form)


class PostDeleteView(StaffRequiredMixin, DeleteView):
    model         = Post
    slug_field    = "slug"
    template_name = "blog/confirm_delete.html"
    success_url   = reverse_lazy("blog:staff_list")
