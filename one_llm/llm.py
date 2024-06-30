from one_llm.models import Models
from one_llm.adapters import Providers
from typing import List, Dict
from dotenv import load_dotenv
load_dotenv()
import os
print(os.environ.get("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY")


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
    
    def chat_completion(self, messages, return_original=False):
        provider = self.get_provider()
        converted_payload = Providers.get_chat_completion_payload(provider, self.get_model(), messages, 512)
        return Providers.make_chat_completion_call(provider, converted_payload, return_original=return_original)

if __name__ == "__main__":

    messages = [{"role":"user", "content":"Hello world"}]

    # print("\n\n\nANTHROPIC Example\n\n\n")

    model_name = "claude-3-haiku-20240307"

    # one_llm = OneLLM(model_name)

    # print(one_llm.chat_completion(messages))

    # print("\n\n\nOPENAI Example\n\n\n")
    # # Switching to an openai model
    model_name = "gpt-4o"

    one_llm = OneLLM(model_name)
    print("\n\n")

    import json
    print(json.dumps(one_llm.chat_completion(messages, return_original=True)))
    # print(result)

    # TODO: return standardized output, flag for return_original_output