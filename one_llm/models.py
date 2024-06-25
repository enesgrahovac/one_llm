from enum import Enum    
from typing import Optional

class Models(Enum):
    CLAUDE_3_HAIKU = "claude-3-haiku-20240307"
    CLAUDE_3_5_SONNET = "claude-3-5-sonnet-20240620"
    CLAUDE_3_OPUS = "claude-3-opus-20240229"
    GPT_4o = "gpt-4o"
    GPT_3_5_turbo = "gpt-3.5-turbo"

    @property
    def cost(self):
        return {
            "claude-3-haiku-20240307": {"input_tokens": 0.00000025, "output_tokens": 0.00000125},
            "claude-3-5-sonnet-20240620": {"input_tokens": 0.00000300, "output_tokens": 0.00001500},
            "claude-3-opus-20240229": {"input_tokens": 0.00001500, "output_tokens": 0.00007500},
            "gpt-4o": {"input_tokens": 0.000005, "output_tokens": 0.000015},
            "gpt-3.5-turbo": {"input_tokens": 0.0000005, "output_tokens": 0.0000015}
        }[self.value]
    
    @property
    def provider(self):
        return {
            "claude-3-haiku-20240307": "anthropic",
            "claude-3-5-sonnet-20240620": "anthropic",
            "claude-3-opus-20240229": "anthropic",
            "gpt-4o": "openai",
            "gpt-3.5-turbo": "openai"
        }[self.value]
    
    @classmethod
    def get_all_models(cls):
        return list(cls)
    
    @classmethod
    def get_model_by_name(cls, model_name: str) -> Optional['Models']:
        if not isinstance(model_name, str):
            raise TypeError(f"model_name must be a string, but got type {type(model_name).__name__}")
        for model in cls:
            if model.value == model_name:
                return model
        return None
    
if __name__ == "__main__":
    all_models = Models.get_all_models()
    for model in all_models:
        print(f"Model: {model.name}, Value: {model.value}, Cost: {model.cost}, Provider: {model.provider}")
