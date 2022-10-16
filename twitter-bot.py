import tweepy, time, sys
import config


def twitter_bot():
    # file from which to read tweets in
    argfile = str(sys.argv[1])

    # number of seconds to wait until next tweet
    seconds = int(sys.argv[2])

    # establish connection to twitter api
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    api = tweepy.API(auth)

    # read in the tweets
    with open(argfile, "r") as file:
        content = file.read()
        tweets = content.split("§§§")

    # publish the tweets
    for tweet in tweets:
        tweet = tweet.strip()
        api.update_status(tweet)
        time.sleep(seconds)  # update status every 15 minutes


if __name__ == "__main__":
    twitter_bot()
