import requests
import tweepy as tw

consumer_key= 'WgTilcUxe5aZUZGCUJ6nrkzcJ'
consumer_secret= '9NFm7vdKAyiC3BDsCK1QF33clGFplDnWU9nvKMqZVH7pf8ATXE'
access_token= '304813303-TCxQMYCys5cBVEFita6yG720nXIWvaXMDhLUDXqI'
access_token_secret= 'Q26BUcwrGvLzmiCMv2bnOkO2GljLWan2fNGQs6TdxMg04'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#USERS_URL = 'http://jsonplaceholder.typicode.com/users'
USERS_URL = tw.API(auth, wait_on_rate_limit=True)


def get_users():
    """Get list of users"""
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None
