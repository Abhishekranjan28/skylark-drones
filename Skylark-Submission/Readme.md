Overview

This project implements an AI-powered Business Intelligence agent that enables founders and executives to ask strategic business questions and receive structured, executive-level insights from live Monday.com data.

The agent dynamically reads:
Deals board (sales pipeline)
Work Orders board (execution)
No CSV data is hardcoded.

Architecture
User Question
      ↓
Gemini Query Planner
      ↓
Deterministic Python Execution
      ↓
Data Quality Scoring
      ↓
Gemini Executive Insight
      ↓
Founder-Level Output

Features
✅ Monday.com Integration

GraphQL API
Read-only
Dynamic data retrieval

✅ Data Resilience

Null normalization
Date parsing
Currency cleaning
Stage normalization
Missing value detection
Forecast confidence scoring

✅ Query Understanding

LLM-generated structured plans
Sector filtering
Time filtering
Cross-board support

✅ Business Intelligence

Revenue analysis
Pipeline health
Sector performance
Execution metrics
Leadership briefings

-->Setup Instructions:

Generate Monday API token
Retrieve board IDs

Add environment variables:
MONDAY_API_TOKEN=...
DEALS_BOARD_ID=...
WORK_ORDERS_BOARD_ID=...
GEMINI_API_KEY=...


-->Install dependencies:
pip install -r requirements.txt


-->Run:
streamlit run app.py

Example Queries
How is our pipeline looking this quarter?
Show revenue for energy sector.
Are we missing critical deal data?
Prepare a leadership update.
What are our biggest risks?
