
from config_ab import *
# from config import *
import json
from time import sleep
from requests_oauthlib import OAuth1Session
import emoji
import os


def remove_emoji(str):
    return ''.join(c for c in str if c not in emoji.UNICODE_EMOJI)


# Get Tweets
def get_tweets(key_word, since, until, loop=1):
    # max 500 tweets are collected
    twitter = OAuth1Session(api_key, api_secret_key, access_token, access_token_secret)

    # see https://developer.twitter.com/en/docs/tweets/search/api-reference/premium-search
    url = 'https://api.twitter.com/1.1/tweets/search/fullarchive/analytic.json'

    tweets = []
    next_page = ''
    os.mkdir('get_tweets')
    fw = open('get_tweets' + "/" + key_word + ".json", "w")

    for i in range(loop):
        # update 'next' to collect tweets more than 100
        if next_page != '':
            params = {
                'query': key_word,  # Search query
                'maxResults': '100',  # number of tweets to get per 1 request. (max: 100)
                # since and until formatted as yyyyMMddHHMM
                'fromDate': since,
                'toDate': until,
                'next': next_page,
            }
        else:
            params = {
                'query': key_word,
                'maxResults': '100',
                'fromDate': since,
                'toDate': until,
            }

        req = twitter.get(url, params=params)


        # access succeeded
        if req.status_code == 200:
            # for API access restriction
            limit = req.headers['x-rate-limit-remaining']
            if limit == 1:
                print('API access is being restricted, stopping.')
                sleep(60 * 15)
                print('Restart.')

            search_tl = json.loads(req.text)  # get search results
            json.dump(search_tl['results'], fw)

            for tweet in search_tl['results']:
                tweets.append(remove_emoji(tweet['text']))
                # print(remove_emoji(tweet['text']))
                # print('---------------------')

            # update next_page if response has key 'next'
            if 'next' in search_tl:
                next_page = search_tl['next']
            else:
                break

        else:
            print("Failed: %d" % req.status_code)

    print("%d Tweets are collected." % len(tweets))
    fw.close()
    return '\n'.join(tweets)


if __name__ == '__main__':
    print(get_tweets('裏垢', '201801010800', '201906091000'))






