import tweepy

def get_twitter_client():
    # Replace with your actual Twitter API credentials
    API_KEY = 'your_api_key'
    API_SECRET_KEY = 'your_api_secret_key'
    ACCESS_TOKEN = 'your_access_token'
    ACCESS_TOKEN_SECRET = 'your_access_token_secret'
    
    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    client = tweepy.API(auth)
    return client


def fetch_user_tweets(username, count=10):
    client = get_twitter_client()
    tweets = client.user_timeline(screen_name=username, count=count, tweet_mode="extended")
    return [{
        "tweet_id": tweet.id_str,
        "created_at": tweet.created_at,
        "text": tweet.full_text,
        "retweets": tweet.retweet_count,
        "likes": tweet.favorite_count
    } for tweet in tweets]