import pandas as pd
import numpy as np
import re


def normalize_board(items):
    rows = []

    for item in items:
        row = {"item_id": item["id"], "item_name": item["name"]}
        for col in item["column_values"]:
            row[col["id"]] = col["text"]
        rows.append(row)

    df = pd.DataFrame(rows)
    df = df.replace(["", "null", "None", "NaN"], np.nan)

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip().str.lower()

    return df


def detect_columns(df):

    def find(keys):
        for col in df.columns:
            for k in keys:
                if k in col:
                    return col
        return None

    return {
        "amount": find(["value", "amount", "deal"]),
        "stage": find(["stage"]),
        "sector": find(["sector", "industry"]),
        "probability": find(["prob"]),
        "close_date": find(["close", "date"])
    }


def clean_amount(df, col):
    if not col or col not in df.columns:
        return df, 0

    df[col] = df[col].astype(str).apply(lambda x: re.sub(r"[^\d.]", "", x))
    numeric = pd.to_numeric(df[col], errors="coerce")

    invalid = numeric.isna().sum()
    df[col] = numeric

    return df, invalid


def clean_dates(df, col):
    if not col or col not in df.columns:
        return df, 0

    parsed = pd.to_datetime(df[col], errors="coerce")
    invalid = parsed.isna().sum()
    df[col] = parsed

    return df, invalid
