import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return (
        customers.merge(orders, left_on="id", right_on="customerId", how="left")
        .loc[lambda x: x.customerId.isna()]
        .rename(columns={"name": "Customers"})[["Customers"]]
    )
