from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, View, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# class Home(ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'posts'
#     ordering = ['-id']

def home(request):
    post = Post.objects.all()
    #paginator
    paginator = Paginator(post, 3)
    page = request.GET.get('page')
    paged_item = paginator.get_page(page)

    return render(request, "blog/home.html", {'posts': paged_item})

class About(View):
    def get(self, request):
        return render(request, 'blog/about.html', )

class PostDetails(DetailView):
    model = Post
    template_name = 'blog/details.html'
    context_object_name = 'post'

class CreatePost(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/newpost.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/deletepost.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UpdatePost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']
    template_name = 'blog/updatepost.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False