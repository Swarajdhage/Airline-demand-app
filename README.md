# ✈️ Airline Booking Market Demand Web App

This web application analyzes and visualizes market demand trends in the airline booking industry — specifically designed for evaluating booking interest in major Australian cities. Built as part of a technical assessment, it demonstrates scraping, API integration, data processing, and web app development using free tools.

---

## 🔍 Features

- ✅ **Trend Data**: Scrapes public interest data from Google Trends using the `pytrends` API
- ✅ **API Integration**: (Optional) Uses OpenAI API to summarize trends and generate insights
- ✅ **Web Interface**: Built with Streamlit for ease of use — no coding knowledge required
- ✅ **Data Processing**: Cleans and visualizes time-series demand trends
- ✅ **Output**: Interactive charts and summaries showing high-demand periods and route popularity

---

## 🛠️ Tech Stack

- Python 3
- Streamlit
- Pandas
- Matplotlib
- PyTrends
- OpenAI (optional)

---

## 🖥️ How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/airline-demand-app.git
cd airline-demand-app
Install dependencies


pip install -r requirements.txt
(Optional) Set OpenAI API Key for AI insights


export OPENAI_API_KEY="your-api-key"
If no key is provided, the app will skip AI-generated summaries.

Run the app


streamlit run app.py

🧪 Example Use Case
Search for a route like "Sydney to Melbourne" or "Brisbane to Perth" to see public interest trends over the last 3 months. The chart reflects real-time demand behavior based on Google search traffic. AI-powered summaries (if enabled) provide quick insights on peak interest periods and demand shifts.

📁 Project Structure
graphql
Copy
Edit
├── app.py               # Main Streamlit app
├── trends.py            # Fetches Google Trends data
├── insights.py          # Optional: uses OpenAI API for summaries
├── requirements.txt     # Python dependencies
└── README.md            # You're reading it!

🧠 Insights Output (Optional)
If you enable the OpenAI API, the app will generate text summaries answering:

Is demand increasing or decreasing?

Are there any spikes?

What are the high-demand periods?

📦 Deployment
This app can be easily deployed for free using Streamlit Cloud.
Just connect this repo, and Streamlit will automatically launch the app.

📬 Contact
Author: Swaraj Dhage
Submitted for: Technical Test Task – Airline Booking Demand Web App
Company: PS Fin Solutions
Evaluator: Shinod

✅ Status
✔️ Task requirements fully implemented and ready for review.
