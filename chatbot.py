# chatbot.py
from sentiment_analysis import analyze_sentiment  # Ensure this matches the function name

class ChatBot:
    def __init__(self):
        self.responses = {
            "hello": "Hi! How can I help you today?",
            "bye": "Goodbye! Have a nice day!",
            "how are you": "I'm just a bot, but I'm doing fine, thanks for asking!"
        }

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # If the user asks for sentiment
        sentiment = analyze_sentiment(user_input)
        if sentiment:
            return f"The sentiment of your message is: {sentiment}"

        # Basic chatbot responses
        return self.responses.get(user_input, "I'm sorry, I don't understand that.")

# Main loop to run the chatbot
def run_chatbot():
    bot = ChatBot()
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == 'bye':
            print(bot.get_response(user_input))
            break
        else:
            print("Bot:", bot.get_response(user_input))

# Run the chatbot
run_chatbot()
