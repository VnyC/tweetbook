import tweepy
import time
print("Welcome back Vinay")

consumer_key = 'wGNE1qCPjhjfcOYMWsOik6g0O'
consumer_secret = 'kF1Y0jVAZviLfvODQVmYJJ3NIQvBkVAoStsqajzvclihcejxDk'

key = '1238345000678653952-qE5mHVLjjYE45Qjfqg2bZBvMsjYelq'
secret = 'E61WoMrFfVgb21ovryHrMr7KNx5mtwMgMxRyhlWJoCJca'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
# api.update_status('All Good things are wild and free!')

filename = 'last_seen.txt'


def read_last_seen(filename):
    file_read = open(filename, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def write_last_seen(filename, last_seen_id):
    file_write = open(filename, 'w')
    file_write.write(str(last_seen_id))
    file_write.close
    return


def reply():
    tweets = api.home_timeline(read_last_seen(filename), tweet_mode='extended')
    for tweet in reversed(tweets):
        try:
            if 'Buddhist' in tweet.full_text.lower():
                print(str(tweet.id)+' - '+tweet.full_text)
                api.update_status('@'+tweet.user.screen_name+' Auto reply and like works https://www.google.com/;)', tweet.id)
                api.create_favorite(tweet.id)
                write_last_seen(filename, tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)

while True:
    reply()
    time.sleep(20)
