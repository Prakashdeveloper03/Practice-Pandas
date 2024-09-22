import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return (
        employees.assign(time_spent=employees["out_time"] - employees["in_time"])
        .groupby(["emp_id", "event_day"])["time_spent"]
        .sum()
        .reset_index()
        .rename(columns={"event_day": "day", "time_spent": "total_time"})
    )
