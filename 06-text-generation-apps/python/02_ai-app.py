import os
from groq import Groq

from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure Groq service client 
client = Groq(
    api_key=os.getenv("GROK_API_KEY"),
)

deployment="llama-3.3-70b-versatile"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
