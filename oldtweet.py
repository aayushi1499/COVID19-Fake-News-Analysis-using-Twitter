import GetOldTweets3 as got
import pandas as pd

keyword = "corona,positive "
oldest_date = "2020-01-01"    
newest_date = "2020-06-10"

tweet_criteria = got.manager.TweetCriteria().setQuerySearch(keyword)\
                                            .setSince(oldest_date)\
                                            .setUntil(newest_date)\
                                            .setTopTweets(True)\
                                            .setMaxTweets(500)
                                            

tweet_df = pd.DataFrame({'got_criteria':got.manager.TweetManager.getTweets(tweet_criteria)})

def get_twitter_info():
    tweet_df["date"] = tweet_df["got_criteria"].apply(lambda x: x.date)
    tweet_df["tweet"] = tweet_df["got_criteria"].apply(lambda x: x.text)
    tweet_df["user"] = tweet_df["got_criteria"].apply(lambda x: x.username)
    tweet_df["retweets"] = tweet_df["got_criteria"].apply(lambda x: x.retweets)
    tweet_df["likes"] = tweet_df["got_criteria"].apply(lambda x: x.favorites)
    tweet_df['hashtags'] = keyword
    return tweet_df

get_twitter_info() 
tweet_df = tweet_df.drop("got_criteria", 1)
print(tweet_df.head(20))
tweet_df.to_csv("Twitter.csv",encoding="utf_8_sig")
