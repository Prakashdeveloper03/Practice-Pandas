import pandas as pd
from typing import List


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(data=student_data, columns=["student_id", "age"])
