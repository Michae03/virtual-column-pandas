import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:

    valid_column = re.compile(r'^[A-Za-z_]+$')
    valid_role = re.compile(r'^[A-Za-z_\s\+\-\*]+$')
    valid_operators = ['+', '-', '*']

    # Validation
    for col in df.columns:
        if not valid_column.fullmatch(col):
            return pandas.DataFrame([])

    if not valid_column.fullmatch(new_column):
        return pandas.DataFrame([])

    if not valid_role.fullmatch(role):
        return pandas.DataFrame([])

    tokens = re.split(r'(\+|\-|\*)', role)
    tokens = [t.strip() for t in tokens if t.strip() != ""]
    if len(tokens) % 2 == 0:
        return pandas.DataFrame([])
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

    # Evaluation
    try:
        new_df = df.copy()

        after_mult = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '*':
                left = after_mult.pop()
                right = df[tokens[i + 1]]
                after_mult.append(left * right)
                i += 2
            else:
                if token not in ['+', '-']:
                    after_mult.append(df[token])
                else:
                    after_mult.append(token)
                i += 1

        result = after_mult[0]
        i = 1
        while i < len(after_mult):
            op = after_mult[i]
            value = after_mult[i + 1]
            if op == '+':
                result += value
            elif op == '-':
                result -= value
            i += 2
        new_df[new_column] = result
        return new_df

    except Exception:
        return pandas.DataFrame([])
