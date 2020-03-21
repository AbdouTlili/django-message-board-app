from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):


    def setUp(self):
        Post.objects.create(text='testCase')

    def test_text_content(self):
        test_post = Post.objects.get(id=1)
        expected_text = f'{test_post.text}'
        self.assertEqual(expected_text,'testCase')
        