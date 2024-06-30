import anthropic
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
)

def message_claude(model, max_tokens, messages):
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=messages
    )
    return message