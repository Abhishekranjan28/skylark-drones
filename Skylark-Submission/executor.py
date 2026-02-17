from datetime import datetime


def filter_time(df, col, period):

    if not col or col not in df.columns:
        return df

    now = datetime.now()

    if period == "current_month":
        start = datetime(now.year, now.month, 1)
        return df[df[col] >= start]

    if period == "current_quarter":
        quarter = (now.month - 1) // 3 + 1
        start_month = 3 * quarter - 2
        start = datetime(now.year, start_month, 1)
        return df[df[col] >= start]

    return df


def execute(plan, deals_df, work_df, columns):

    board = plan["board"]
    analysis = plan["analysis"]
    filters = plan.get("filters", {})

    df = deals_df if board == "deals" else work_df

    # Sector
    sector_col = columns.get("sector")
    if filters.get("sector") and sector_col:
        df = df[df[sector_col] == filters["sector"].lower()]

    # Time
    df = filter_time(df, columns.get("close_date"), filters.get("time_period"))

    amount = columns.get("amount")
    stage = columns.get("stage")

    if analysis == "pipeline":
        return {"total_pipeline": df[amount].sum() if amount else 0}

    if analysis == "revenue" and stage:
        closed = df[df[stage].str.contains("won", na=False)]
        return {"revenue": closed[amount].sum() if amount else 0}

    if analysis == "execution":
        return {"total_projects": len(df)}

    if analysis == "leadership":
        return {
            "pipeline": df[amount].sum() if amount else 0,
            "records": len(df)
        }

    return {"message": "No valid analysis"}
