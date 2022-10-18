import tweepy, time, sys
import config

def twitter_bot():
    # establish connection to twitter api
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    api = tweepy.API(auth)

    temp = '' 
    tweets = []

    # read in the tweets
    with open('example.txt', "r") as file:
        content = file.read()
    
    for char in content:
        if char == '~':
            tweets.append(temp)
            temp = ''
        else:
            temp += char
    tweets.append(temp)
    print(tweets)        

    # publish the tweets
    for tweet in tweets:
        tweet = tweet.strip()
        print(tweet)
        api.update_status(tweet)
        time.sleep(2*60)  # update status every 2 minutes


if __name__ == "__main__":
    twitter_bot()
