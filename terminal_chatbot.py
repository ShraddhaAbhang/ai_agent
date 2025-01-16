import openai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Load OpenAI API key from environment variables
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("OpenAI API key not found. Please set the API_KEY environment variable.")

openai.api_key = API_KEY

def gpt4_chatbot():
    """
    A simple terminal-based chatbot using OpenAI's GPT-4 API.
    Users can input messages, and the chatbot responds based on GPT-4's output.
    """
    print("Welcome to GPT-4 Terminal Chatbot! Type 'exit' to quit.")

    # Initialize the conversation history
    conversation = []

    while True:
        # User input
        user_input = input("You: ").strip()

        # Exit condition
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Append user input to the conversation history
        conversation.append({"role": "user", "content": user_input})

        try:
            # Call GPT-4 API
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=conversation
            )

            # Extract GPT-4's reply
            gpt_reply = response['choices'][0]['message']['content'].strip()
            
            # Print GPT-4's reply
            print(f"GPT-4: {gpt_reply}")

            # Append GPT-4's reply to the conversation history
            conversation.append({"role": "assistant", "content": gpt_reply})
        
        except Exception as e:
            print(f"Error: {e}")

# Run the chatbot
gpt4_chatbot()
