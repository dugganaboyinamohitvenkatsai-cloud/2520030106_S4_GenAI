from llm_client import ask_gemini, ask_ollama


print("=== LLM Client ===")
print("1. Gemini")
print("2. Ollama")

choice = input("\nChoose provider (1/2): ")
prompt = input("Enter your question: ")

if choice == "1":
    answer = ask_gemini(prompt)

elif choice == "2":
    answer = ask_ollama(prompt)

else:
    print("Invalid choice.")
    exit()

print("\nLLM Response:")
print(answer)