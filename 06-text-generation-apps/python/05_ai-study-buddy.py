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
question = input("Ask your questions on python language to your study buddy: ")
prompt = f"""
You are an expert on the python language.

Whenever certain questions are asked, you need to provide response in below format.

- Concept
- Example code showing the concept implementation
- explanation of the example and how the concept is done for the user to understand better.

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
