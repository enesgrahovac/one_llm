class OpenAI:
    @staticmethod
    def chat_completion_payload(model, messages, system_message):
        return {
            "model": model,
            "messages": messages,
            "system_message": system_message
        }
    
    @staticmethod
    def make_chat_completion_call(payload):
        print("making request to OpenAI API with this payload: ", payload)
        response = {"response": "placeholder"}
        return response
