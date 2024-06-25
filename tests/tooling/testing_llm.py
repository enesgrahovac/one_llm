from one_llm.llm import OneLLM



if __name__ == "__main__":
    model_name = "claude-3-haiku-20240307"
    one_llm = OneLLM(model_name)
    print(f"Model: {model_name}, Provider: {one_llm.get_provider()}")

    # Tests

    # This isn't a correct model name
    model_name = 42
    try:
        one_llm = OneLLM(model_name)
    except Exception as e:
        print(e)

    # This model doesn't exist
    model_name = "claude-3-haiku-20240308"
    one_llm = OneLLM(model_name)
    print(f"Model: {model_name}, Provider: {one_llm.get_provider()}")