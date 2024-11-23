from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SocialAccount(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	platform = models.CharField(max_length=50)
	access_token = models.CharField(max_length=255)


class SocialPost(models.Model):
	"""docstring for SocialAccount"""
	account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE)
	post_id = models.CharField(max_length=100)
	text = models.TextField()
	created_at = models.DateTimeField()
	engagement_rate = models.FloatField(default=0.0)
	sentiment_score = models.FloatField(default=0.0)

class TwitterAccount(models.Model):
    username = models.CharField(max_length=255, unique=True)
    profile_image = models.ImageField(upload_to='post_images', blank=True, null=True)
    
class Tweet(models.Model):
    account = models.ForeignKey(TwitterAccount, on_delete=models.CASCADE, related_name='tweets')
    tweet_id = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    created_at = models.DateTimeField()
    retweets = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.account.username} - {self.text[:50]}"
		