# filepath: /workspace/kids-art/blog/management/commands/truncate_titles.py
from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Truncate titles to fit the new maximum length constraint'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        for post in posts:
            if len(post.title) > 50:
                post.title = post.title[:50]
                post.save()
        self.stdout.write(self.style.SUCCESS('Successfully truncated titles'))