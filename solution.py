import pandas as pd


def add_virtual_column(df, role, new_column):
    if role.count("+") != 1:
        return pd.DataFrame()

    left_column, right_column = role.split("+")

    if left_column not in df.columns or right_column not in df.columns:
        return pd.DataFrame()

    result = df.copy()
    result[new_column] = result[left_column] + result[right_column]

    return result
