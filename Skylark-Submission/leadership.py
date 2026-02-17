def leadership_briefing(pipeline, revenue, execution, quality):

    briefing = {
        "Revenue Closed": revenue,
        "Total Pipeline": pipeline["total_pipeline"],
        "Weighted Pipeline": pipeline["weighted_pipeline"],
        "Win Rate (%)": pipeline["win_rate_pct"],
        "Execution Completion Rate (%)": execution,
        "Forecast Confidence Score": quality["forecast_confidence_score"]
    }

    return briefing
