class Anthropic:
    @staticmethod
    def chat_completion_payload(model, messages, system_message):
        return {
            "model": model,
            "inputs": messages,
            "context": system_message
        }
    
    @staticmethod
    def make_chat_completion_call(payload):
        print("making request to Anthropic API with this payload: ", payload)
        response = {"response": "placeholder"}
        return response