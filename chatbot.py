
import csv
import os
from datetime import datetime

import ollama

# Project settings
MODEL = "llama3.2"
DATASET_DIR = "dataset"

HISTORY_FILE = os.path.join(DATASET_DIR, "chat_history.csv")
RESPONSES_FILE = os.path.join(DATASET_DIR, "responses.csv")
LOG_FILE = os.path.join(DATASET_DIR, "chatbot_logs.txt")

os.makedirs(DATASET_DIR, exist_ok=True)

# Create CSV files with headings if they do not exist
def initialize_csv(filename):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "user_question", "chatbot_response"])

initialize_csv(HISTORY_FILE)
initialize_csv(RESPONSES_FILE)

# Conversation history for context-aware responses
history = [
    {
        "role": "system",
        "content": (
            "You are EduBot, a helpful education chatbot. "
            "Explain topics in simple language suitable for students. "
            "Give accurate, clear and concise answers. "
            "If you are unsure, say so instead of inventing facts."
        )
    }
]

def save_conversation(question, answer, timestamp):
    # Save the full conversation record to chat_history.csv
    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, question, answer])

    # Save question and response to responses.csv
    with open(RESPONSES_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, question, answer])

    # Save a readable copy to the text log
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"\nTimestamp: {timestamp}\n")
        file.write(f"User: {question}\n")
        file.write(f"EduBot: {answer}\n")
        file.write("-" * 50 + "\n")

def main():
    print("=" * 50)
    print("       EduBot - Education Chatbot")
    print("       Powered by Ollama and Llama 3.2")
    print("Type 'exit' to stop the chatbot.")
    print("=" * 50)

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("EduBot: Goodbye! Keep learning.")
            break

        if not question:
            print("EduBot: Please enter a question.")
            continue

        # Add the user's message to conversation history
        history.append({"role": "user", "content": question})

        try:
            response = ollama.chat(
                model=MODEL,
                messages=history
            )

            answer = response.message.content.strip()

            # Add the assistant's reply to history
            history.append({
                "role": "assistant",
                "content": answer
            })

            print(f"\nEduBot: {answer}")

            timestamp = datetime.now().astimezone().isoformat(
                timespec="seconds"
            )
            save_conversation(question, answer, timestamp)

        except ollama.ResponseError as error:
            print(f"Model error: {error}")
            history.pop()  # Remove unanswered user message

        except Exception as error:
            print(f"Error connecting to Ollama: {error}")
            print("Check that Ollama is running and the model is installed.")
            history.pop()  # Remove unanswered user message

if __name__ == "__main__":
    main()
