import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].str.match(r"^[a-zA-Z][a-zA-Z\d_.-]*@leetcode\.com")]
