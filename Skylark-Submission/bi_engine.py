import pandas as pd


def compute_pipeline_metrics(df, columns):

    amount_col = columns.get("amount")
    stage_col = columns.get("stage")
    prob_col = columns.get("probability")

    if not amount_col or amount_col not in df.columns:
        return {"error": "Deal amount column not detected in Deals board."}

    # Clean numeric values
    df[amount_col] = (
        df[amount_col]
        .astype(str)
        .str.replace(r"[^\d.]", "", regex=True)
    )

    df[amount_col] = pd.to_numeric(df[amount_col], errors="coerce")

    total_pipeline = df[amount_col].sum()

    weighted_pipeline = total_pipeline

    if prob_col and prob_col in df.columns:
        df[prob_col] = pd.to_numeric(df[prob_col], errors="coerce")
        weighted_pipeline = (
            df[amount_col] * df[prob_col] / 100
        ).sum()

    win_rate = 0

    if stage_col and stage_col in df.columns:
        won = df[df[stage_col].str.contains("won", na=False)]
        win_rate = round((len(won) / len(df)) * 100, 2) if len(df) else 0

    return {
        "total_pipeline": round(total_pipeline, 2),
        "weighted_pipeline": round(weighted_pipeline, 2),
        "win_rate_pct": win_rate
    }
