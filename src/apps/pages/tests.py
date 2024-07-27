from django.test import TestCase
from django.urls import resolve, reverse

from apps.channels.models.app import App
from apps.channels.models.channel import Channel
from apps.users.models import User


class HomePageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@teste.com', password='12345')
        self.app = App.objects.create(user=self.user, name='Test App')
        self.channel = Channel.objects.create(
            app=self.app, channel_type='web_push', enabled=True)
        self.client.login(email='test@teste.com', password='12345')

    def test_home_page_url_resolves(self):
        self.assertEqual(reverse('home_page'), '/')
        self.assertEqual(resolve('/').view_name, 'home_page')

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        """
        Verify that unauthenticated users are redirected to the login page.
        """
        self.client.logout()
        response = self.client.get(reverse('home_page'))
        self.assertRedirects(response, reverse('account_login'))

    def test_home_page_accessible_for_logged_in_user(self):
        """
        Verify that the home page is accessible for authenticated users.
        """
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_context_data_contains_apps(self):
        """
        Verify that the home page context contains the correct app data.
        """
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        context = response.context

        # Check if 'apps' is in the context
        self.assertIn('apps', context)
        apps = context['apps']

        # Verify that 'apps' contains the test app
        self.assertTrue(any(app['id'] == self.app.id for app in apps))
        self.assertTrue(any(app['name'] == self.app.name for app in apps))
        self.assertTrue(any(any(
            self.channel.id == c.id for c in app['channels']
        ) for app in apps))

        # Check if the channel is associated with the correct app
        self.assertTrue(any(
            c for app in apps for c in app['channels'] if c.id == self.channel.id
        ))
