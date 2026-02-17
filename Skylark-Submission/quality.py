def compute_quality(df, columns, invalid_amounts, invalid_dates):

    total = len(df)
    report = {"total_records": total}

    amount = columns.get("amount")
    date = columns.get("close_date")
    prob = columns.get("probability")

    if amount:
        report["missing_amount_pct"] = round(
            df[amount].isna().sum() / total * 100, 2
        )

    if date:
        report["missing_close_date_pct"] = round(
            df[date].isna().sum() / total * 100, 2
        )

    if prob and prob in df.columns:
        report["missing_probability_pct"] = round(
            df[prob].isna().sum() / total * 100, 2
        )

    confidence = 100
    confidence -= report.get("missing_amount_pct", 0) * 0.4
    confidence -= report.get("missing_close_date_pct", 0) * 0.3
    confidence -= report.get("missing_probability_pct", 0) * 0.2
    confidence -= invalid_amounts * 0.05
    confidence -= invalid_dates * 0.05

    report["forecast_confidence_score"] = max(round(confidence, 2), 0)

    return report


def build_caveat(report):

    notes = []

    if report.get("missing_amount_pct", 0) > 10:
        notes.append("Significant missing deal values.")

    if report.get("missing_close_date_pct", 0) > 10:
        notes.append("Many deals missing close dates.")

    if report.get("forecast_confidence_score", 100) < 80:
        notes.append("Forecast confidence moderate.")

    if not notes:
        return "Data quality strong."

    return " | ".join(notes)
