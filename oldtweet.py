import GetOldTweets3 as got
import pandas as pd

keyword = "corona,positive,arvind kejriwal "

oldest_date = "2020-06-01"    
newest_date = "2020-06-10"
number_tweets = 70

tweet_criteria = got.manager.TweetCriteria().setQuerySearch(keyword)\
                                            .setSince(oldest_date)\
                                            .setUntil(newest_date)\
                                            .setTopTweets(True)\
                                            .setMaxTweets(number_tweets)
                                            

tweet_df = pd.DataFrame({'got_criteria':got.manager.TweetManager.getTweets(tweet_criteria)})

def get_twitter_info():
    tweet_df["date"] = tweet_df["got_criteria"].apply(lambda x: x.date)
    tweet_df["tweet"] = tweet_df["got_criteria"].apply(lambda x: x.text)
    tweet_df["user"] = tweet_df["got_criteria"].apply(lambda x: x.username)
    # tweet_df["location"] = tweet_df["got_criteria"].apply(lambda x: x.geolocation)
    tweet_df["retweets"] = tweet_df["got_criteria"].apply(lambda x: x.retweets)
    tweet_df["likes"] = tweet_df["got_criteria"].apply(lambda x: x.favorites)
    tweet_df['hashtags'] = keyword
    # tweet_df["link"] = tweet_df["got_criteria"].apply(lambda x: x.permalink)

    return tweet_df

get_twitter_info() 
tweet_df = tweet_df.drop("got_criteria", 1)
print(tweet_df.head(20))
tweet_df.to_csv("Twitter.csv",encoding="utf_8_sig")