import time
import tweepy

access_token='834827659301548032-oUwoBugbBIkFGhB33dWpBcBM7Mq1ilc'
access_token_secret='t3qEwq3UrssGJGJhc1VGHp8QF2GT8EVcoVAvWjFSUJSlQ'
consumer_key='AlcWde3wizrQPlXquNXajnAJ8'
consumer_secret='Xvf0DBUHj1m8JOHLVsnXGMAipAOVoY67RUHVIwU6dggNYlNe8K'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, api_root = '/1.1', wait_on_rate_limit = True, wait_on_rate_limit_notify = True, compression = True)

name1=raw_input("dwse ton prwto xristi twitter")


name2=raw_input("dwse ton deutero xristi twitter")

ids= api.followers_ids(name1)
ids2= api.followers_ids(name2);

finallid= set(ids).intersection(ids2)

finalusers=[]
for i in finallid:
    finalusers.append(api.get_user(i).name)

for i in finalusers:
    print i.encode('utf8')
