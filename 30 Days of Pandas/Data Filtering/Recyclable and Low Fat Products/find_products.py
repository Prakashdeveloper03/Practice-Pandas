import pandas as pd


def find_products(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["low_fats"] == "Y") & (df["recyclable"] == "Y")][["product_id"]]
