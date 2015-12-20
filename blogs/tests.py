from django.test import TestCase, RequestFactory
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User
from .views import post_list
from .models import Post

class SimpleTest(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()   
        # create a user
        self.user = User.objects.create_superuser(
            username = 'adminTest',
            email='test@email.com',
            password='password'
        )   

    def create_post(self, title="view test", text="this is a view test"):
        return Post.objects.create(author=self.user, title=title, text=text, published_date=timezone.now())
    
    def test_post_list_view(self):
        p = self.create_post()
        self.assertTrue(isinstance(p, Post))
        
        # Create an instance of a GET request.
        request = self.factory.get('/post_list')
        # Test post_list() as if it were deployed at /post_lists
        response = post_list(request)
        self.assertEqual(response.status_code, 200)

# models test
# don't know how to access self.user if here I separate tests into two classes

#class PostModelsTest(TestCase):

    def test_saving_and_retrieving_posts(self):
        firstPost = Post()
        firstPost.author = self.user
        firstPost.title = "First Post"
        firstPost.text = "This is the 1st Post"
        firstPost.published_date = timezone.now()
        firstPost.save()

        secondPost = Post()
        secondPost.author = self.user
        secondPost.title = "Second Post"
        secondPost.text = "This is the 2nd Post"
        secondPost.published_date = timezone.now()
        secondPost.save()

        thirdPost = Post()
        thirdPost.author = self.user
        thirdPost.title = "Final Post"
        thirdPost.text = "This is the 3nd Post"
        thirdPost.published_date = timezone.now()
        thirdPost.save()

        saved_posts = Post.objects.all()
        self.assertEqual(saved_posts.count(), 3)

        first_saved_post = saved_posts[0]
        second_saved_post = saved_posts[1]
        third_saved_post = saved_posts[2]

        self.assertEqual(first_saved_post.title, 'First Post')
        self.assertNotEqual(firstPost.published_date, timezone.now())
