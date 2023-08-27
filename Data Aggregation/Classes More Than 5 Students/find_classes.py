import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grouped = courses.groupby("class")["student"].count().reset_index()
    grouped = grouped[grouped["student"] >= 5]
    return grouped[["class"]]
