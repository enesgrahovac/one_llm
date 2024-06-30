from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
print(os.environ.get("OPENAI_API_KEY"), "OPENAI_API_KEY")
client = OpenAI(
    # os.environ.get("OPENAI_API_KEY")
)

def message_openai(model, max_tokens, messages):

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens
    )
    
    return response