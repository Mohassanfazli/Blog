from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse
from .forms import NewPostForm
from .models import Post
from django.views import generic
from django.urls import reverse_lazy


# def Post_list_view(request):
#     Posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/Posts_list.html', {'Posts_list': Posts_list})  # second  is contex for html

class PostListView(generic.ListView):

    template_name = 'blog/Posts_list.html'
    context_object_name = 'Posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')




# def Post_detail_view(request, pk):
#     Posts = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/Posts_detail.html', {'Post': Posts})

class PostDetailView (generic.DetailView):
    model = Post
    template_name = 'blog/Posts_detail.html'
    context_object_name = 'Post'


# def Post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Posts_list')  # Redirect after saving
#         else:
#             print(form.errors)
#
#     else:
#         form = NewPostForm()
#
#     return render(request, 'blog/Post_create.html', context={'form': form})

class PostCreateView (generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/Post_create.html'

def Post_update_view(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance= posts)

    if form.is_valid():
        form.save()
        return redirect('Posts_list')
    return render(request, 'blog/Post_create.html', {'form': form})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/Post_create.html'

class DeletePostView(generic.DetailView):
    model = Post
    template_name = 'blog/Posts_Delete.html'
    success_url = '/blog'




