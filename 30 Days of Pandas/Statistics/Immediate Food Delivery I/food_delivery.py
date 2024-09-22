import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "immediate_percentage": [
                round(
                    (
                        (
                            delivery["order_date"]
                            == delivery["customer_pref_delivery_date"]
                        ).sum()
                        / delivery.shape[0]
                    )
                    * 100,
                    2,
                )
            ],
        }
    )
