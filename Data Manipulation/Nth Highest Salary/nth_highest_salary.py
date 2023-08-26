import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    return (
        employee.sort_values(
            by="salary",
            ascending=False,
        )
        .drop_duplicates(
            subset=["salary"],
        )
        .iloc[N - 1 : N][["salary"]]
    )
