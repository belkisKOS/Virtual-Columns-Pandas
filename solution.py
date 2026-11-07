import re

import pandas as pd


def _is_valid_label(label):
    return (
        isinstance(label, str)
        and re.fullmatch(r"[A-Za-z_]+", label) is not None
    )


def add_virtual_column(df, role, new_column):
    if not isinstance(role, str) or not _is_valid_label(new_column):
        return pd.DataFrame()

    if not all(_is_valid_label(column) for column in df.columns):
        return pd.DataFrame()

    if role.count("+") == 1:
        operator = "+"
    elif role.count("-") == 1:
        operator = "-"
    elif role.count("*") == 1:
        operator = "*"
    else:
        return pd.DataFrame()

    left_column, right_column = role.split(operator)
    left_column = left_column.strip()
    right_column = right_column.strip()

    if not _is_valid_label(left_column) or not _is_valid_label(right_column):
        return pd.DataFrame()

    if left_column not in df.columns or right_column not in df.columns:
        return pd.DataFrame()

    result = df.copy()

    if operator == "+":
        result[new_column] = result[left_column] + result[right_column]
    elif operator == "-":
        result[new_column] = result[left_column] - result[right_column]
    elif operator == "*":
        result[new_column] = result[left_column] * result[right_column]

    return result
