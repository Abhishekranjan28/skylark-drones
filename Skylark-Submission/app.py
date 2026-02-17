import streamlit as st
import os
from dotenv import load_dotenv
from monday_client import fetch_board
from cleaning import normalize_board, detect_columns, clean_amount, clean_dates
from quality import compute_quality, build_caveat
from planner import generate_plan
from executor import execute
from llm import generate_summary

load_dotenv()

st.set_page_config(layout="wide")
st.title("🚀 Elite Monday BI Agent")

DEALS_ID = os.getenv("DEALS_BOARD_ID")
WORK_ID = os.getenv("WORK_ORDERS_BOARD_ID")

with st.form("form"):
    query = st.text_input("Ask a founder-level business question:")
    submit = st.form_submit_button("Submit")

if submit and query:

    with st.spinner("Analyzing business data..."):

        deals_raw = fetch_board(DEALS_ID)
        work_raw = fetch_board(WORK_ID)

        deals_df = normalize_board(deals_raw)
        work_df = normalize_board(work_raw)

        columns = detect_columns(deals_df)

        deals_df, invalid_amounts = clean_amount(
            deals_df, columns.get("amount")
        )

        deals_df, invalid_dates = clean_dates(
            deals_df, columns.get("close_date")
        )

        quality_report = compute_quality(
            deals_df, columns, invalid_amounts, invalid_dates
        )

        caveat = build_caveat(quality_report)

        plan = generate_plan(query)

        if not plan:
            st.error("Could not interpret question. Please rephrase.")
            st.stop()

        metrics = execute(plan, deals_df, work_df, columns)

        summary = generate_summary(query, metrics, caveat)

    st.markdown("## 📊 Executive Insight")
    st.write(summary)

    with st.expander("🔎 Transparency"):
        st.json({
            "Plan": plan,
            "Metrics": metrics,
            "Data Quality": quality_report
        })
