from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# Post model
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)  # Title with max 50 characters
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', blank=False, null=False)  # Make image field required
    content = models.CharField(max_length=150)  # Content with max 150 characters
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]  # orders the comments by descending order, with last comment on top and first on bottom 
        
    def __str__(self):
        return f"{self.title} | written by {self.author}"

# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()    
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Comment {self.body} by {self.author}"

# filepath: /workspace/kids-art/blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 50}),
            'content': forms.Textarea(attrs={'maxlength': 150}),
        }
