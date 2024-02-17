# Improved Chat Bot Solution
# -------------------------------------------------------------
# 1) Install the required packages
#    pip install ChatterBot chatterbot_corpus spacy
#    python3 -m spacy download en_core_web_sm
#    Or... choose the language you prefer
# -------------------------------------------------------------
# 2) Import necessary modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# 3) Function to create and run the chat bot
def create_chat_bot():
    # Create a ChatBot instance
    chatbot = ChatBot('Chattering Bot')

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot on the English language corpus
    trainer.train('chatterbot.corpus.english')

    # Inform user about the chatbot
    print("Chattering Bot: Hello! I'm ready to chat. Type 'exit' to end the conversation.")

    # Continuous conversation loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Check for exit command
        if user_input.lower() == 'exit':
            print("Chattering Bot: Goodbye!")
            break

        # Get and print bot response
        bot_response = chatbot.get_response(user_input)
        print("Chattering Bot:", bot_response)

# 4) Main entry point
if __name__ == '__main__':
    create_chat_bot()
