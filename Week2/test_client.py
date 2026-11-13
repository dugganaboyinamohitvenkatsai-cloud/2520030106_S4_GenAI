from llm_client import ask_gemini, ask_ollama


def test_ollama():
    response = ask_ollama("Say hello in one short sentence.")
    assert response
    print("Ollama test passed.")


def test_gemini():
    response = ask_gemini("Say hello in one short sentence.")
    assert response
    print("Gemini test passed.")


if __name__ == "__main__":
    test_ollama()
    test_gemini()
    print("\nAll tests passed.")