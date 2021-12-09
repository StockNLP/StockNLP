import requests

#USERS_URL = 'http://jsonplaceholder.typicode.com/users'
USERS_URL = 'https://api.pushshift.io/reddit/search/comment'


def get_users():
    """Get list of users"""
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None
