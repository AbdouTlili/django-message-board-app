from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='testCase')

    def test_text_content(self):
        test_post = Post.objects.get()
        expected_text = f'{test_post.text}'
        self.assertEqual(expected_text,'testCase')



class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='testCase')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res,'home.html')
        