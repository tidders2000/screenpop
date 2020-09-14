from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import CommentForm, add_blog_form
from .models import Post
from django.contrib import messages


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 3


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def add_blog(request):
    if request.method == "POST":
        blogAdd = add_blog_form(request.POST, request.FILES)
        if blogAdd.is_valid():
            blogAdd.save(commit=True)
            messages.error(request, "News Added")
    else:
        blog = add_blog_form()
    return render(request, 'add_blog.html', {'blog': blog})
