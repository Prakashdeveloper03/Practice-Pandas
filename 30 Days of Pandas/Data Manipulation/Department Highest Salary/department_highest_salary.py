import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    return (
        employee.merge(
            department,
            left_on="departmentId",
            right_on="id",
            suffixes=("_employee", "_department"),
        )
        .groupby("departmentId")
        .apply(lambda x: x[x["salary"] == x["salary"].max()])
        .reset_index(drop=True)[["name_department", "name_employee", "salary"]]
        .rename(
            columns={
                "name_department": "Department",
                "name_employee": "Employee",
                "salary": "Salary",
            }
        )
    )
