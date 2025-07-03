# insights.py
import openai
import os

# You must set your API key like this before running:
# os.environ["OPENAI_API_KEY"] = "your-api-key"

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_insights(df, route):
    if openai.api_key is None:
        return "⚠️ No API key provided. AI-generated insights disabled."

    data_points = df.reset_index().to_dict(orient='records')
    
    prompt = (
        f"Given the following time-series search trend data for airline route '{route}', "
        "analyze the data and summarize:\n"
        "- If demand is rising or falling\n"
        "- Any noticeable spikes\n"
        "- Estimated high-demand periods\n\n"
        f"Data:\n{data_points[:30]}\n\n"
        "Write a short, readable summary."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=250,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating insights: {str(e)}"
