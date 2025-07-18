import google.generativeai as genai

GOOGLE_API_KEY = "your_api_key"

genai.configure(api_key=GOOGLE_API_KEY)

async def analyze_with_gemini(data, sector):
    model = genai.GenerativeModel(model_name = 'models/gemini-1.5-flash')
    prompt = f"""Analyze the following market data for the {sector} sector in India and extract trade opportunities. Format the response as a markdown report.

Data:
{data}
"""
    response = model.generate_content(prompt)
    return response.text