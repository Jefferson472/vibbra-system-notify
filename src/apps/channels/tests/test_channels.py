from django.test import TestCase
from django.urls import resolve, reverse

from apps.channels.models.app import App
from apps.channels.models.channel import Channel
from apps.users.models import User


class ChannelListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@teste.com', password='testpassword')
        self.client.login(username='test@teste.com', password='testpassword')

        self.app = App.objects.create(name='Test App', user=self.user)
        self.other_app = App.objects.create(name='Another App', user=self.user)
        self.channel1 = Channel.objects.create(
            app=self.app, channel_type='web_push', enabled=True)
        self.channel2 = Channel.objects.create(
            app=self.app, channel_type='email', enabled=False)
        self.channel3 = Channel.objects.create(
            app=self.other_app, channel_type='sms', enabled=True)

    def test_channels_list_url_resolves(self):
        self.assertEqual(reverse('channels_list', kwargs={"app_id": 1}), '/channels/1/')
        self.assertEqual(resolve('/channels/1/').view_name, 'channels_list')

    def test_channel_list_view_authenticated(self):
        url = reverse('channels_list', kwargs={'app_id': self.app.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'channels/channel_list.html')

        # Check if the correct channels are in the context
        self.assertIn('object_list', response.context)
        channels = response.context['object_list']
        self.assertIn(self.channel1, channels)
        self.assertIn(self.channel2, channels)
        # Channel from a different app should not be included
        self.assertNotIn(self.channel3, channels)

    def test_redirect_if_not_authenticated(self):
        # Test that the view redirects if the user is not authenticated
        self.client.logout()
        url = reverse('channels_list', kwargs={'app_id': self.app.id})
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_channel_delete_view(self):
        channels_count = Channel.objects.count()

        url = reverse('channel_delete', kwargs={'pk': self.channel1.id})
        response = self.client.post(url, follow=True)

        self.assertEqual(Channel.objects.count(), channels_count - 1)
        self.assertRedirects(
            response,
            reverse('channels_list', kwargs={'app_id': self.channel1.app.id})
        )
