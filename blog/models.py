from django.db import models
#To add current time to posts based on UTC in settings.py
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        '''
        Any one can comment on a post, but all of them not gonna get approved,
        This method filters out unapproved(approved_comment = False) comments from Comment class,
        So that only approved(approved_comment = True) comments save to the model 'Post'
        '''
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        '''
        After Someone creates a post, the user need to be taken to the posts
        detailed view page('post_detail'),
        Detailed view always needs the primary key(pk) to display/identify the post
        'self.pk' represents return to the detailed view of same post after creating
        '''
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name = 'comments',on_delete = models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        '''
        To approve a comment and save to db
        '''
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        '''
        return to the list view(ie the homepage) after commenting on
        a post, the comments needs approval to display
        '''
        return reverse("post_list")

    def __str__(self):
        return self.text
