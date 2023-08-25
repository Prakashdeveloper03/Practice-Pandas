import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.where(tweets.content.str.len() > 15).loc[
        lambda x: x.tweet_id.notna()
    ][["tweet_id"]]
