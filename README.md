# Virtual Column Expression Parser (Pandas Task)

## Overview

This solution implements a function that adds a new computed (virtual) column to a pandas DataFrame based on a simple arithmetic expression provided as a string.

---

## Features

* Supports basic arithmetic operations:

  * Addition (`+`)
  * Subtraction (`-`)
  * Multiplication (`*`)
* Handles operator precedence (`*` is evaluated before `+` and `-`)
* Validates input expression and column names
* Safe evaluation (no use of `eval`)
* Returns an empty DataFrame for invalid input

---

## Function Description

```python
add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame
```

### Parameters:

* `df` – input pandas DataFrame
* `role` – arithmetic expression using column names (e.g. "A + B * C")
* `new_column` – name of the new column to be created

### Returns:

* A new DataFrame with an additional computed column
* Empty DataFrame (`pandas.DataFrame([])`) if validation fails

---

## Example Usage

```python
import pandas

from solution import add_virtual_column

# Sample data

df = pandas.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})

# Create new column using expression

result = add_virtual_column(df, "A + B * C", "D")

print(result)
```
---

## Safety Considerations

This implementation avoids using Python's `eval()` function to ensure safe execution. All expressions are parsed and evaluated manually.

---
