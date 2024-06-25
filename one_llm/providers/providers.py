from .openai import OpenAI
from .anthropic import Anthropic

class Providers:
    @staticmethod
    def get_chat_completion_payload(provider: str, model_name, messages, system_message):
        if provider == "openai":
            return OpenAI.chat_completion_payload(model_name, messages, system_message)
        elif provider == "anthropic":
            return Anthropic.chat_completion_payload(model_name, messages, system_message)
        else:
            raise ValueError(f"Provider '{provider}' not supported")
        
    def make_chat_completion_call(provider: str, payload: dict):
        if provider == "openai":
            return OpenAI.make_chat_completion_call(payload)
        elif provider == "anthropic":
            return Anthropic.make_chat_completion_call(payload)
        else:
            raise ValueError(f"Provider '{provider}' not supported")
