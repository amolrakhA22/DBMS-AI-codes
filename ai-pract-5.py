# Simple Chatbot in Python

# Define responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm a bot, so I don't have feelings, but thanks for asking!",
    "help": "I'm here to assist! You can ask me about the weather, time, or general info.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Happy to help.",
    "weather": "Sorry, I can't fetch live data, but you can check your local weather online.",
    "time": "I don't have a clock, but you can check your device for the current time!"
}

# Main Chatbot function
def chatbot():
    print("Hello! I'm Chatbot. Type 'bye' to end the conversation.")
    while True:
        # Get user input
        user_input = input("You: ").lower()  # Convert to lowercase to handle case sensitivity
        
        # Check if the input matches any keyword
        if user_input in responses:
            print("Chatbot:", responses[user_input])
            if user_input == "bye":
                break  # Exit the chat if user says "bye"
        else:
            print("Chatbot: Sorry, I didn't understand that. Could you rephrase?")

# Run the chatbot
chatbot()
