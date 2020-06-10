import csv
import re
from twitter import Twitter,OAuth
import config

twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret),secure=True)


csvFile = open('analysis.csv', 'w',encoding="utf_8_sig")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['TIMESTAMP','USERNAME','LOCATION','TWEETS','LIKES','RETWEETS'])
keyword=('#COVID19 #cowdung')

query = twitter.search.tweets(q=("#vaccine OR #WHO"),count=15,lang="en",include_entities=True,encoding="utf-8",tweet_mode="extended",until="2020-06-04")

for result in query["statuses"]:
    try:
        dates = result["created_at"]
        text = result["full_text"]
        user = re.findall(r'(RT +@\w+\:)',text) 
        # for url in result["entities"]["urls"]:
        #     urls = print(" - found URL: %s" % url["expanded_url"])
        location = result['user']['location']
        tweet = result['retweeted_status']["full_text"]
        likes = result["retweet_count"]
        retweets = result['retweeted_status']['favorite_count']
        
        texts = re.sub(r'^.*?RT @[A-Za-z0-9_]*:', '',text)
        print("\n%s %s  %s \n%s  \nLikes %s \nRetweets %s" % (dates,user,location,tweet, retweets ,likes))
        csvWriter.writerow([dates,user,location,tweet, retweets ,likes])

    except KeyError:
        print("")
