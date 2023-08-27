import pandas as pd


def sales_person(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
    return (
        sales_person[
            ~sales_person["sales_id"].isin(
                orders[
                    orders["com_id"] == int(company[company["name"] == "RED"].com_id)
                ].sales_id
            )
        ][["name"]]
        if "RED" in company["name"].values
        else sales_person[["name"]]
    )
