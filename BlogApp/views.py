from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#dummy data
# dummyposts = [
#     {
#         'author': 'Ameya Keskar',
#         'title': 'I am done XD',
#         'content': 'This is my first ever blog post. I am going to write my heart out in this post. HAHAHAH.. That\'s it for today.',
#         'date': 'Today', 
#     },
#     {
#         'author': 'Mocha Pom',
#         'title': 'I have 1Mil on YT',
#         'content': 'I am a cute pomerian and I have 1mil on YT. What do you have? huh?!',
#         'date': 'Yesterday', 
#     },
# ]

# Create your views here.
def home(request):
    context = {'posts' : Post.objects.all()}
    return render(request, 'Blog/BlogHome.html', context)

class PostListView(ListView):
    model = Post

    #after calling as_view() Dango will be looking for the following view, by default
    #<appName>/<model>_<viewtype>.html
    template_name = 'Blog/BlogHome.html'
    context_object_name = 'posts'
    ordering = ['-date_created'] #ordering of posts, based on date
    paginate_by = 2
class PostDetailView(DetailView):
    model = Post
    template_name = 'Blog/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Blog/post_form.html'

    #override the form_valid method, for setting post auther as current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Blog/post_form.html'

    #override the form_valid method, for setting post auther as current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Post 
    template_name = 'Blog/post_confirm_delete.html'
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'Blog/BlogAbout.html', {'title': 'This is the title'})