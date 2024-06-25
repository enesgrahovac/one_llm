Switch LLM Api providers with 1 line of code 🤖🪄

```python
print("\n\n\nANTHROPIC Example\n\n\n")
model_name = "claude-3-haiku-20240307"
one_llm = OneLLM(model_name)
anthropic_response = one_llm.chat_completion([{"role":"user", "content":"Hello world"}], "Hello, how are you?")
print(anthropic_response)

print("\n\n\nOPENAI Example\n\n\n")
# Switching to an openai model
model_name = "gpt-4o"
one_llm = OneLLM(model_name)
openai_response =  one_llm.chat_completion([{"role":"user", "content":"Hello world"}], "Hello, how are you?")
print(openai_response)
```

This example shows how you can switch from an Anthropic model to an OpenAI model with a single line of code change.

