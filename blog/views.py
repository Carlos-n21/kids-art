from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 8  # Show 8 posts per page


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_id = request.POST.get("comment_id")  # 👈 Get comment ID if it's an update

        if comment_id:
            # Updating existing comment
            comment_instance = get_object_or_404(Comment, id=comment_id, author=request.user)
            comment_form = CommentForm(data=request.POST, instance=comment_instance)
        else:
            # Creating new comment
            comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.approved = True
            comment.save()

            messages.add_message(request, messages.SUCCESS, 'Comment submitted successfully')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    else:
        comment_form = CommentForm()

    return render(
        request, "blog/post_detail.html", 
        {
            "post": post, 
            "comments": comments,        
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )



def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()  # No need to reset approval status
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    post.delete()
    return redirect('profile')

@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user, status=1).order_by('-created_on')
    paginator = Paginator(user_posts, 8)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/profile.html', {'posts': page_obj, 'is_paginated': page_obj.has_other_pages()})

@login_required
def approve_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__author=request.user)
    comment.approved = True
    comment.save()
    return redirect('profile')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__author=request.user)
    comment.delete()
    return redirect('profile')

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query, status=1) if query else None
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})

def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'post_detail', args=['blog']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )

def test_successful_collaboration_request_submission(self):
    """Test for a user requesting a collaboration"""
    post_data = {
        'name': 'test name',
        'email': 'test@email.com',
        'message': 'test message'
    }
    response = self.client.post(reverse('about'), post_data)
    self.assertEqual(response.status_code, 200)
    self.assertIn(
        b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)