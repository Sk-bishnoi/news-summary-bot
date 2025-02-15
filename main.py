# src/python/app/app.py

import streamlit as st
from datetime import datetime
from src.python.app.utils.utils import fetch_news, get_last_n_days
from src.python.app.constant.constants import CATEGORIES
from reportlab.pdfgen import canvas
import io


st.title("📰 AI-Powered News Aggregator")

# Sidebar: Select Date Range & Category
start_date, end_date = get_last_n_days()
date_range = st.date_input("Select Date Range", [datetime.strptime(start_date, '%Y-%m-%d'), datetime.strptime(end_date, '%Y-%m-%d')])
selected_categories = st.multiselect("Select Categories", options=list(CATEGORIES.keys()), default=["International"])

# Fetch and display news
if st.button("Fetch News"):
    news_data = []
    for category in selected_categories:
        news_data += fetch_news(category, date_range[0].strftime('%Y-%m-%d'), date_range[1].strftime('%Y-%m-%d'))

    if news_data:
        for article in news_data:
            st.subheader(article["title"])
            st.write(article["summary"])
            st.write("---")
    else:
        st.write("No news found.")

# PDF Report Generation
def generate_pdf(news_data):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle("News Report")

    y_position = 750
    pdf.drawString(100, y_position, "AI-Generated News Report")
    pdf.drawString(100, y_position - 20, f"Date Range: {date_range[0]} to {date_range[1]}")
    y_position -= 40

    for article in news_data:
        if y_position < 50:
            pdf.showPage()
            y_position = 750
        pdf.drawString(100, y_position, f"Title: {article['title']}")
        pdf.drawString(100, y_position - 20, f"Summary: {article['summary']}")
        y_position -= 40

    pdf.save()
    buffer.seek(0)
    return buffer

if st.button("Generate PDF Report"):
    if news_data:
        pdf_buffer = generate_pdf(news_data)
        st.download_button("Download Report", pdf_buffer, "news_report.pdf", "application/pdf")
    else:
        st.write("No news data available for PDF generation.")
