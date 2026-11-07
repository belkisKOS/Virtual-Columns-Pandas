import pandas as pd

from solution import add_virtual_column


def test_preserves_original_dataframe_and_integer_dtype():
    df = pd.DataFrame({
        "left_value": [2, 5],
        "right_value": [3, 4],
    })
    original = df.copy(deep=True)
    expected = pd.DataFrame({
        "left_value": [2, 5],
        "right_value": [3, 4],
        "total": [5, 9],
    })

    result = add_virtual_column(
        df,
        "left_value + right_value",
        "total",
    )

    assert result.equals(expected)
    assert df.equals(original)


def test_rejects_malformed_roles():
    df = pd.DataFrame({
        "left_value": [2],
        "right_value": [3],
    })

    invalid_roles = (
        "left_value/right_value",
        r"left_value \ right_value",
        "left&value + right_value",
        "left_value + right_value * left_value",
        "left_value++right_value",
    )

    for role in invalid_roles:
        assert add_virtual_column(df, role, "total").empty


def test_rejects_invalid_new_column_labels():
    df = pd.DataFrame({
        "left_value": [2],
        "right_value": [3],
    })

    for new_column in ("total1", "total value", "total&", "", None):
        assert add_virtual_column(
            df,
            "left_value + right_value",
            new_column,
        ).empty


def test_rejects_invalid_dataframe_column_labels():
    df = pd.DataFrame({
        "bad-label": [2],
        "right_value": [3],
    })

    result = add_virtual_column(
        df,
        "right_value + right_value",
        "total",
    )

    assert result.empty
