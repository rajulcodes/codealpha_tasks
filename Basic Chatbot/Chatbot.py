import re # Import the regular expression module for more flexible text matching
import random # Ensure random is imported at the top for consistent use

def clean_input(user_input):
    """
    Cleans the user's input by converting it to lowercase,
    removing leading/trailing whitespace, and stripping punctuation.
    This helps in matching predefined rules more effectively.
    """
    cleaned_text = user_input.lower().strip()
    # Remove common punctuation marks from the end of the input
    # This regex handles multiple punctuation marks at the end
    cleaned_text = re.sub(r'[.,!?;:]+$', '', cleaned_text)
    return cleaned_text

def get_response(user_message):
    """
    Determines the chatbot's response based on the cleaned user message.
    This function uses a series of if-elif-else statements to match patterns
    and return a predefined reply.
    """
    cleaned_message = clean_input(user_message)

    # --- Greetings ---
    if cleaned_message in ["hello", "hi", "hey", "hola", "good morning", "good afternoon", "good evening"]:
        return random.choice(["Hi there!", "Hello!", "Hey!", "Greetings!", "Nice to meet you!", "What can I do for you today?"])

    # --- How are you? ---
    elif "how are you" in cleaned_message or "how's it going" in cleaned_message or "you doing" in cleaned_message:
        return random.choice([
            "I'm doing great, thanks for asking!",
            "I'm fine, thanks for checking in!",
            "All good here, and ready to assist!",
            "As an AI, I don't have feelings, but I'm functioning perfectly!",
            "Couldn't be better!"
        ])

    # --- What is your name? ---
    elif "what is your name" in cleaned_message or "who are you" in cleaned_message or "your name" in cleaned_message:
        return random.choice([
            "I am a simple rule-based chatbot, designed to assist you.",
            "You can call me Chatbot.",
            "I don't have a personal name, I'm an AI.",
            "I am your friendly neighborhood chatbot!"
        ])

    # --- About the weather (simple example) ---
    elif "weather" in cleaned_message or "is it raining" in cleaned_message or "temperature" in cleaned_message:
        return random.choice([
            "I don't have access to real-time weather information, but I hope it's pleasant wherever you are!",
            "My sensors don't pick up weather data. Perhaps check a weather app!",
            "I'm not equipped to tell you about the weather, unfortunately."
        ])

    # --- About feelings/emotions ---
    elif "i am fine" in cleaned_message or "i'm good" in cleaned_message or "i'm okay" in cleaned_message:
        return random.choice([
            "That's good to hear!",
            "Glad to know you're doing well!",
            "Fantastic! Keep up the good spirits."
        ])
    elif "i am sad" in cleaned_message or "i'm feeling down" in cleaned_message or "i'm not good" in cleaned_message:
        return random.choice([
            "I'm sorry to hear that. Is there anything I can do to help?",
            "I hope things get better for you soon.",
            "Sometimes a good chat helps. What's on your mind?",
            "Sending positive vibes your way!"
        ])
    elif "i am happy" in cleaned_message or "i'm excited" in cleaned_message:
        return random.choice([
            "That's wonderful to hear!",
            "Awesome! What makes you happy?",
            "Happiness is contagious!",
            "Keep that positive energy going!"
        ])

    # --- Questions about capabilities ---
    elif "what can you do" in cleaned_message or "help me" in cleaned_message or "can you help" in cleaned_message:
        return random.choice([
            "I can respond to basic greetings, answer simple questions, and engage in a short conversation. Try asking me 'how are you?' or 'what is your name?'",
            "I'm here to chat and respond to a variety of common phrases.",
            "My abilities are currently limited to predefined responses, but I'm always learning!",
            "Ask me anything basic, and I'll do my best to respond!"
        ])

    # --- Thank you ---
    elif "thank you" in cleaned_message or "thanks" in cleaned_message or "appreciate it" in cleaned_message:
        return random.choice(["You're welcome!", "No problem!", "Glad to help!", "Anytime!", "My pleasure!", "Happy to assist!"])

    # --- Asking for time ---
    elif "what time is it" in cleaned_message or "time now" in cleaned_message:
        return "I don't have access to real-time clock information. You can check your device's time."

    # --- Asking about origin ---
    elif "where are you from" in cleaned_message or "who created you" in cleaned_message:
        return random.choice([
            "I exist in the digital realm.",
            "I was created by a developer using Python.",
            "I don't have a physical location."
        ])

    # --- Random small talk / filler ---
    elif "what's up" in cleaned_message or "sup" in cleaned_message:
        return random.choice(["Not much, just here to chat!", "The sky!", "Just processing information.", "What's up with you?"])
    elif "tell me a joke" in cleaned_message:
        return random.choice([
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fish with no eyes? Fsh!",
            "I'm not very good at telling jokes, but I can try!"
        ])
    elif "how old are you" in cleaned_message:
        return "I don't have an age in the human sense. I'm a program!"

    # --- Affirmative/Negative responses ---
    elif cleaned_message in ["yes", "yeah", "yep", "sure"]:
        return random.choice(["Okay!", "Understood.", "Got it!"])
    elif cleaned_message in ["no", "nope", "nah"]:
        return random.choice(["Alright.", "Understood.", "Okay, then."])

    # --- Farewell ---
    elif cleaned_message in ["bye", "goodbye", "see you", "exit", "quit", "farewell"]:
        return random.choice(["Goodbye!", "See you later!", "Farewell!", "Have a great day!", "It was nice chatting with you!", "Until next time!"])

    # --- Default/Fallback Response ---
    else:
        return random.choice([
            "I'm not sure I understand. Can you rephrase that?",
            "That's interesting! Could you tell me more?",
            "My apologies, I can only handle a limited set of queries.",
            "Please try asking something else.",
            "Could you elaborate on that?",
            "I'm still learning, so I might not understand everything.",
            "Hmm, I need more data to respond to that."
        ])

def start_chatbot():
    """
    Initiates and manages the main conversation loop of the chatbot.
    The chatbot will continue to respond until the user types a farewell message.
    """
    print("--- Welcome to the Expanded Basic Chatbot! ---")
    print("Type 'bye' or 'quit' to end the conversation.")
    
    while True: # Loop indefinitely until a break condition is met
        user_input = input("\nYou: ") # Get input from the user
        
        # Check for exit commands before cleaning, to allow direct exit
        # This ensures that even if 'bye' has punctuation, it's caught
        if clean_input(user_input) in ["bye", "goodbye", "see you", "exit", "quit", "farewell"]:
            response = get_response(user_input) # Get a farewell response
            print(f"Chatbot: {response}")
            break # Exit the loop, ending the conversation
        
        # Get the chatbot's response for other inputs
        chatbot_response = get_response(user_input)
        print(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    start_chatbot()
