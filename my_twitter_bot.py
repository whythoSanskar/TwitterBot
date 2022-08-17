import tweepy
import keys_test

def api():
    auth = tweepy.OAuthHandler(keys_test.API_KEY, keys_test.API_SECRET)
    auth.set_access_token(keys_test.ACCESS_TOKEN, keys_test.ACCEESS_TOKEN_SECRET)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweetwd successfully!')


if __name__ == "__main__":
    api = api()
    tweet(api, 'This tweeet was tweeted from Python')

# print('this is my twitter bot')

# # CONSUMER_KEY= 'AAAAAAAAAAAAAAAAAAAAAOhOgAEAAAAARxoEwrO%2FeR9GXUbMADhwCbX1vc8%3DuLd9oKBT83AMFXO44CoEAKx9Ij1i1uK29YqmooGUfDMT1FTtgO'

# # ACCESS_KEY = 'LwKeoe3poxgQ2HCpPiN5f9bNs'
# # ACCESS_SECRET = 'iUJvPXAJvhVhAvBaqBMI1rNaY2RrkyPiQqZ4uuS6pFLGGKX3G7'

# auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAOhOgAEAAAAARxoEwrO%2FeR9GXUbMADhwCbX1vc8%3DuLd9oKBT83AMFXO44CoEAKx9Ij1i1uK29YqmooGUfDMT1FTtgO")
# # auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# api = tweepy.API(auth)




