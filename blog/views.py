from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .forms import CommentForm, add_blog_form
from .models import Post, Comment
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.core.paginator import Paginator


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog.html'
#     paginate_by = 3

def post_list(request):
    post_list = Post.objects.all().order_by('-created_on')
    paginator = Paginator(post_list, 5)  # Show 5 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Post.objects.order_by('tag').distinct('tag')
    popular = Post.objects.order_by('updated_on')
    cat_list = Post.objects.order_by('category').distinct('category')
    if request.method == "POST":
        keyword = request.POST.get('keyword')

        # type = request.POST.get('type')
        post_list = Post.objects.filter(
            Q(author__first_name__icontains=keyword) | Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(author__last_name__icontains=keyword))

    return render(request, "blog.html", {'page_obj': page_obj, 'popular': popular, 'post_list': post_list, 'tags': tags, 'cat_list': cat_list})


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    other_posts = Post.objects.filter(author=post.author)

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
                                           'comment_form': comment_form,
                                           'other_posts': other_posts

                                           })


def add_blog(request):
    history = Post.objects.filter(author=request.user)
    if request.method == "POST":
        blog = add_blog_form(request.POST, request.FILES)
        if blog.is_valid():
            sb = blog.save(commit=False)
            sb.author = request.user
            sb.slug = slugify(sb.title)
            sb.save()
            messages.error(request, "Blog Added")
    else:
        blog = add_blog_form()
    return render(request, 'add_blog.html', {'blog': blog, 'history': history})


def post_tag(request):
    tag = request.GET['q']
    post_list = Post.objects.filter(tag=tag)
    return render(request, 'blog.html', {'post_list': post_list})


def edit_post(request, pk):
    history = Post.objects.filter(author=request.user)
    data = Post.objects.get(pk=pk)
    blog = add_blog_form(instance=data)
    if request.method == "POST":
        a = Post.objects.get(pk=pk)
        f = add_blog_form(request.POST, instance=a)
        f.save()
        return redirect(reverse('add_blog'))
        messages.error(request, "News Added")
    else:
        messages.error(request, 'error')

    return render(request, 'edit_blog.html', {'blog': blog, 'history': history})
