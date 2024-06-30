from one_llm.apis.anthropic import message_claude
from one_llm.utils.json_conversion import _convert_to_serializable

class Anthropic:
    @staticmethod
    def chat_completion_payload(model, messages, max_tokens):
        return {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens
        }
    
    @staticmethod
    def make_chat_completion_call(payload):
        claude_response = message_claude(payload["model"], payload["max_tokens"], payload["messages"])
        claude_response_json = _convert_to_serializable(claude_response)
        return claude_response_json
    
    @staticmethod
    def convert_message_to_unified_output(messages):
        formatted_messages = []
        for message in messages:
            formatted_message = {
                "content": message["text"],
                "role": "assistant"
            }
            formatted_messages.append(formatted_message)
        return formatted_messages
    
    @staticmethod
    def convert_to_unified_output(response):
        unified_output = {
            "id": response["id"],
            "choices": Anthropic.convert_message_to_unified_output(response["content"]),
            "model": response["model"],
            "usage": response["usage"]
        }
        
        return unified_output