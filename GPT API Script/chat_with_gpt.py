import openai
import os


def load_chat_history():
    history = []
    if os.path.exists("chat_history.txt"):
        with open("chat_history.txt", "r") as file:
            history = file.read().splitlines( )
    return history


def save_chat_history(messages):
    with open("chat_history.txt", "w") as file:
        for message in messages:
            file.write(f"{message}\n")

def chat():
    openai.api_key = "-"

    # Load chat history
    chat_history = load_chat_history()
    messages = []
    for line in chat_history:
        role = "user" if chat_history.index(line) % 2 == 0 else "system"
        messages.append({"role": role, "content": line})

    while True:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=messages
        )
        ai_message = response['choices'][0]['message']['content'].strip( )
        print(f"GPT: {ai_message}")
        messages.append({"role": "system", "content": ai_message})


        save_chat_history([msg['content'] for msg in messages if msg['role'] == "user"] +
                          [msg['content'] for msg in messages if msg['role'] == "system"])

        if user_input.lower() == "quit":
            break


if __name__ == "__main__":
    chat()


























