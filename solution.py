import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:

    valid_column = re.compile(r'^[A-Za-z_]+$')
    valid_role = re.compile(r'^[A-Za-z_\s\+\-\*]+$')
    valid_operators = ['+', '-', '*']

    # Input validation
    for col in df.columns:
        if not valid_column.fullmatch(col):
            return pandas.DataFrame([])

    if not valid_column.fullmatch(new_column):
        return pandas.DataFrame([])

    if not valid_role.fullmatch(role):
        return pandas.DataFrame([])

    tokens = re.split(r'(\+|\-|\*)', role)
    tokens = [t.strip() for t in tokens if t.strip() != ""]
    if not tokens:
        return pandas.DataFrame([])
    if tokens[0] in valid_operators or tokens[-1] in valid_operators:
        return pandas.DataFrame([])
    for i, token in enumerate(tokens):
        if i % 2 == 0:
            if token in valid_operators:
                return pandas.DataFrame([])
            if token not in df.columns:
                return pandas.DataFrame([])
        else:
            if token not in valid_operators:
                return pandas.DataFrame([])

    # new_column evaluation
    try:
        new_df = df.copy()
        # I used pandas.eval for expression evaluation.
        # The input is strictly validated (only letters, underscores, and + - * operators),
        # which prevents code injection and ensures safe evaluation.
        new_df[new_column] = df.eval(role)
        return new_df
    except Exception:
        return pandas.DataFrame([])

    # Alternative approach (not used here) would be to manually parse and evaluate
    # the expression without using eval for full control over execution.