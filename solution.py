import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:

    valid_column = re.compile(r'^[A-Za-z_]+$')
    valid_role = re.compile(r'^[A-Za-z_\s\+\-\*]+$')
    valid_operators = ['+', '-', '*']

    # columns validation
    for col in df.columns:
        if not valid_column.fullmatch(col):
            return pandas.DataFrame([])

    # new_columns validation
    if not valid_column.fullmatch(new_column):
        return pandas.DataFrame([])

    # role characters validation
    if not valid_role.fullmatch(role):
        return pandas.DataFrame([])

    # role structure validation
    tokens = re.split(r'(\+|\-|\*)', role)
    tokens = [t.strip() for t in tokens if t.strip() != ""]
    if not tokens:
        return pandas.DataFrame([])
    if tokens[0] in valid_operators:
        return pandas.DataFrame([])
    if tokens[-1] in valid_operators:
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

   # new_columns evaluation
    try:
        new_df = df.copy()
        new_df[new_column] = df.eval(role)
        return new_df
    except Exception:
        return pandas.DataFrame([])
