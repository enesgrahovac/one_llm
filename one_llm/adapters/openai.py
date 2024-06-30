from one_llm.apis.openai import message_openai
from one_llm.utils.json_conversion import _convert_to_serializable

class OpenAI:

    @staticmethod
    def chat_completion_payload(model, messages, max_tokens):
        return {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens
        }
    
    @staticmethod
    def make_chat_completion_call(payload):
        print("making request to OpenAI API with this payload: ", payload)
        openai_response = message_openai(payload["model"], payload["max_tokens"], payload["messages"])
        openai_response_json = _convert_to_serializable(openai_response)
        return openai_response_json
    
    @staticmethod
    def convert_message_to_unified_output(messages):
        formatted_messages = []
        for message in messages:
            message = message["message"]
            formatted_message = {
                "content": message["content"],
                "role": message["role"]
            }
            formatted_messages.append(formatted_message)
        return formatted_messages
    
    @staticmethod
    def convert_to_unified_output(response):
        unified_output = {
            "id": response["id"],
            "choices": OpenAI.convert_message_to_unified_output(response["choices"]),
            "model": response["model"],
            "usage": response["usage"]
        }
        # {'id': 'chatcmpl-9ffew0AwCL8tbJuMkHbGSKuLI8h50', 'choices': [{'finish_reason': 'stop', 'index': 0, 'logprobs': None, 'message': {'content': 'Hello! How can I assist you today?', 'role': 'assistant', 'function_call': None, 'tool_calls': None}}], 'created': 1719718614, 'model': 'gpt-4o-2024-05-13', 'object': 'chat.completion', 'service_tier': None, 'system_fingerprint': 'fp_d576307f90', 'usage': {'completion_tokens': 9, 'prompt_tokens': 9, 'total_tokens': 18}
        # {'id': 'msg_01XnzA1RPgpCDdkueprgDrZR', 'content': [{'text': "Hello! I'm an AI assistant created by Anthropic. I'm here to help with a variety of tasks. How can I assist you today?", 'type': 'text'}], 'model': 'claude-3-haiku-20240307', 'role': 'assistant', 'stop_reason': 'end_turn', 'stop_sequence': None, 'type': 'message', 'usage': {'input_tokens': 9, 'output_tokens': 34}
        return unified_output