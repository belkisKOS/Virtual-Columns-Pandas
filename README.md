# Virtual Columns in Pandas

## About the project

This project creates a virtual column in a copy of a pandas DataFrame. The new column can add, subtract, or multiply two existing columns.

The function uses `df.copy()` to preserve the original DataFrame.

## Supported operations

The `role` argument describes the calculation:

- Addition: `column_one + column_two`
- Subtraction: `column_one - column_two`
- Multiplication: `column_one * column_two`

Spaces before, after, or around the operator are allowed.

## Validation

Column labels can contain only letters and underscores.

The function returns an empty DataFrame when:

- A column label contains an invalid character
- `new_column` has an invalid name
- The role contains an unsupported or malformed operation
- A referenced column does not exist
- An existing DataFrame column has an invalid label

## Example

```python
import pandas as pd

from solution import add_virtual_column


sales = pd.DataFrame({
    "quantity": [10, 3],
    "price": [10, 1],
})

result = add_virtual_column(
    sales,
    "quantity * price",
    "total",
)

print(result)
```

Output:

```text
   quantity  price  total
0        10     10    100
1         3      1      3
```

The original `sales` DataFrame remains unchanged.

## Installation

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Running the tests

Run all tests with:

```bash
pytest -q
```

The project includes the supplied tests and additional edge-case tests.
