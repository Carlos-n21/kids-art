from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post, Comment


class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post.objects.create(
            title="Blog title",
            author=self.user,
            slug="blog-title",
            content="Blog content",
            status=1
        )

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse('post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 302)  # Assuming a redirect on successful comment submission
        # Verify that the comment was created
        comments = Comment.objects.filter(post=self.post, body='This is a test comment.')
        self.assertEqual(comments.count(), 1)
        self.assertTrue(comments.first().approved)  # Assuming comments need approval
