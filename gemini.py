import google.generativeai as genai
from chaves_api import api


genai.configure(api_key=api["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(
    "compare as 3 datas: 23/09/2023, 04/08/2024, 14/08/2024, qual delas é mais proxima do dia 16/08/2024"
)
print(response.text)
