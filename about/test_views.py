from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Kids-Art",
            content=(
                "Welcome to Kids-Art, a delightful digital gallery where your "
                "child's creativity comes to life! At Kids-Art, we "
                "believe that "
                "every piece of art tells a unique story, and we're here to "
                "celebrate the boundless imagination of young artists "
                "everywhere."
            )
        )
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Kids-Art', response.content)
        self.assertIn(b'Welcome to Kids-Art', response.content)
        self.assertIn(b'Our Mission', response.content)
        self.assertIn(b'How It Works', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm
        )

    def test_submit_collaborate_form(self):
        """Verifies form submission for collaboration"""
        form_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'I would like to collaborate.'
        }
        response = self.client.post(reverse('about'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Assuming a redirect
        # Add more assertions as needed to verify form processing
