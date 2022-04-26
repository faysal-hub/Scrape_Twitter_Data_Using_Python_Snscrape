import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

#Search for the Hashtags
query = "(from:elonmusk) until:2022-04-26 since:2008-01-01"


#modified the query for the output file name
pattern = "[#|:](\w+)"
out = re.sub("^:", "", re.search(pattern, query).group())



# Creating list to append tweet data to
tweets_list = []

#Set the limit here
limit = 50


# Using TwitterSearchScraper to scrape data and append tweets to list
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets_list) == limit:
        break
    else:
        tweets_list.append(
            [tweet.url, tweet.date, tweet.user.username, tweet.user.id, tweet.user.displayname, 
            tweet.user.location, tweet.user.description, tweet.user.verified, tweet.user.followersCount, 
            tweet.user.friendsCount, tweet.user.statusesCount, tweet.user.favouritesCount, tweet.content, 
             tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.lang])




# Creating a dataframe from the tweets list above
df = pd.DataFrame(tweets_list, columns=['Url', 'Date', 'User', 'Id', 'Displayname', 'Location', 'Description', 
                                        'Verified', 'Followers', 'Following','Total_Tweets', 'Total_likes', 
                                        'Tweet', 'Replays', 'Retweets', 'Likes', 'Language'])


# to save to csv
df.to_csv('@{0}.csv'.format(out))
