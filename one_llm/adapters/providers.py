from .openai import OpenAI
from .anthropic import Anthropic
import json

class Providers:

    @staticmethod
    def get_chat_completion_payload(provider: str, model_name, messages, num_tokens):
        if provider == "openai":
            return OpenAI.chat_completion_payload(model_name, messages, num_tokens)
        elif provider == "anthropic":
            return Anthropic.chat_completion_payload(model_name, messages, num_tokens)
        else:
            raise ValueError(f"Provider '{provider}' not supported")    
        
    @staticmethod
    def make_chat_completion_call(provider: str, payload: dict, return_original: bool=False):
        if provider == "openai":
            original_response =  OpenAI.make_chat_completion_call(payload)
            unified_output = OpenAI.convert_to_unified_output(original_response)
        elif provider == "anthropic":
            original_response = Anthropic.make_chat_completion_call(payload)
            unified_output = Anthropic.convert_to_unified_output(original_response)
        else:
            raise ValueError(f"Provider '{provider}' not supported")
        
        function_response = {"response": unified_output}

        if return_original:
            function_response["original_response"] = original_response

        return function_response
