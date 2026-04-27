import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#  FIX 1: Correct env variable name 
client = Groq(api_key=os.getenv("groq_api_key"))

def get_response(messages):
    try:
        response = client.chat.completions.create(
            #  FIX 2: Use active model (old one was decommissioned)
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            max_tokens=512
        )

        return response.choices[0].message.content

    except Exception as e:
        # FIX 3: Prevent crash + show readable error
        return f"Error: {str(e)}"