from django.test import TestCase
from django.urls import resolve, reverse

from apps.channels.models import App
from apps.users.models import User


class AppViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com', password='testpassword')
        self.client.login(email='test@test.com', password='testpassword')
        self.url = reverse('app_create')

    def test_app_create_url_resolves(self):
        self.assertEqual(reverse('app_create'), '/app/create/')
        self.assertEqual(resolve('/app/create/').view_name, 'app_create')

    def test_app_creation_view(self):
        # Check the view is accessible and the form works as expected
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/app_form.html')

        # Create a new app
        response = self.client.post(self.url, {'name': 'Test App'})
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertTrue(App.objects.filter(name='Test App', user=self.user).exists())

        # Check the redirect URL
        app = App.objects.get(name='Test App')
        self.assertRedirects(
            response,
            reverse('channels_list', kwargs={'app_id': app.id})
        )

    def test_redirect_if_not_authenticated(self):
        # Test that the view redirects if the user is not authenticated
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_form_valid_sets_user(self):
        # Check that the form_valid method sets the user correctly
        self.client.post(self.url, {'name': 'Test App'})
        app = App.objects.get(name='Test App')
        self.assertEqual(app.user, self.user)
