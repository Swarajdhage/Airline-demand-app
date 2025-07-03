# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from trends import get_trend_data
from insights import generate_insights

st.set_page_config(page_title="Airline Booking Demand Insights", layout="wide")

st.title("✈️ Airline Booking Market Demand Web App")
st.write("Analyze public demand for different flight routes using search trend data.")

# User input
route = st.text_input("Enter a flight route (e.g., 'Sydney to Melbourne')", "Sydney to Melbourne")

if route:
    with st.spinner("Fetching trend data..."):
        data = get_trend_data(route)

    if not data.empty:
        st.subheader(f"📈 Search Trends for: {route}")
        st.line_chart(data)

        st.subheader("🔍 AI-Generated Insights")
        summary = generate_insights(data, route)
        st.markdown(summary)
    else:
        st.warning("No data found for this route.")
