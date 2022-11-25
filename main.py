import os
import json
import time
import requests

USER_FIELDS = "created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld"


def bearer_oauth(r):
    # To set your environment variables in your terminal run the following line:
    # export 'BEARER_TOKEN'='<your_bearer_token>'
    bearer_token = os.environ.get("BEARER_TOKEN")
    r.headers["Authorization"] = "Bearer {}".format(bearer_token)

    return r


# DOCS: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username
def find_user_id(username):
    url = "https://api.twitter.com/2/users/by/username/{}".format(username)
    url += "?user.fields={}".format(USER_FIELDS)
    response = requests.get(url, auth=bearer_oauth)
    return response.json()["data"]["id"]


# DOCS: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers
def get_followers_page(user_id, next_token=None):
    # URL of the endpoint
    url = "https://api.twitter.com/2/users/{}/followers".format(user_id)
    url += "?max_results=1000&user.fields={}".format(USER_FIELDS)

    # if there is a next_token, add it to the url
    if next_token:
        url += "&pagination_token={}".format(next_token)

    # make the request
    response = requests.get(url, auth=bearer_oauth)

    # if rate limit is reached, wait 15 minutes and try again
    if response.status_code == 429:
        print("Rate limit reached, waiting 5 minutes")
        time.sleep(5 * 60)
        return get_followers_page(user_id, next_token)

    return response.json()


def get_followers(user_id):
    followers = []
    next_token = None
    while True:
        response = get_followers_page(user_id, next_token)
        followers.extend(response["data"])
        if "next_token" in response["meta"]:
            next_token = response["meta"]["next_token"]
        else:
            break

    return followers


# save struct as json
def save_followers(followers, filename):
    with open(filename + ".json", "w") as f:
        json.dump(followers, f, indent=4)


def pre_compute_followers(usernames):

    # get the followers for each account
    for username in usernames:
        user_id = find_user_id(username)
        followers = get_followers(user_id)
        save_followers(followers, str(user_id))


usernames = [
    "thedigitaldogs",
    "CryptoDickbutts",
    "0n1force",
    "kaijukingz",
    "overlord_xyz",
]

pre_compute_followers(usernames)

