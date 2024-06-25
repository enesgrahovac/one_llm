from one_llm.models import Models
from one_llm.providers import Providers
from typing import List, Dict
class OneLLM:
    def __init__(self, model_name: str):
        model = Models.get_model_by_name(model_name)
        if model is None:
            raise ValueError(f"Model '{model_name}' not found")
        self.model = model

    def get_provider(self):
        return self.model.provider

    def get_model(self):
        return self.model.value
    
    def chat_completion(self, messages, system_message):
        provider = self.get_provider()
        converted_payload = Providers.get_chat_completion_payload(provider, self.get_model(), messages, system_message)
        return Providers.make_chat_completion_call(provider, converted_payload)

if __name__ == "__main__":
    print("\n\n\nANTHROPIC Example\n\n\n")
    model_name = "claude-3-haiku-20240307"
    one_llm = OneLLM(model_name)


    print(one_llm.chat_completion([{"role":"user", "content":"Hello world"}], "Hello, how are you?"))

    print("\n\n\nOPENAI Example\n\n\n")
    # Switching to an openai model
    model_name = "gpt-4o"
    one_llm = OneLLM(model_name)


    print(one_llm.chat_completion([{"role":"user", "content":"Hello world"}], "Hello, how are you?"))