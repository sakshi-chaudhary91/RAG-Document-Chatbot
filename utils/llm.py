from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_answer(context, question):

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question only using the context provided below.

If the answer is not present in the context, reply:
"I couldn't find the answer in the document."

Context:
{context}

Question:
{question}
"""
    
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
        return response.text 
    except Exception as e:
        error = str(e)
        if "429" in error:
            return "⚠️ API quota exceeded. Please try again later."
        elif "API_KEY" in error or "401" in error:
            return "🔑 Invalid API Key."
        elif "503" in error:
            return "🌐 Gemini service is temporarily unavailable."
        else:
            return f"❌ Something went wrong: {error}"

       