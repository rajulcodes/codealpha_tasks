# Chatbot: Rule-Based Conversational Assistant

This is a basic rule-based chatbot developed in Python. It demonstrates fundamental concepts of natural language processing, user input handling, control structures, and random response generation.

## Features

* Recognizes common greetings and replies.
* Responds to questions like:

  * "How are you?"
  * "What is your name?"
  * "Where are you from?"
* Handles basic emotional expressions (happy, sad, fine).
* Supports small talk (jokes, weather, time inquiries).
* Includes a clean input parser to standardize user inputs.
* Uses `random` to return varied replies for the same inputs.
* Gracefully exits when the user types farewell commands (e.g., `bye`, `quit`).

## Technologies Used

* Python 3
* `re` for regular expressions
* `random` for randomized responses

## How to Run the Chatbot

1. Make sure Python 3 is installed.
2. Save the chatbot code in a file named `chatbot.py`.
3. Open your terminal or command prompt.
4. Run the script:

   ```bash
   python chatbot.py
   ```
5. Chat with the bot! Type `bye` or `quit` to end the conversation.

## Example Interaction

```
--- Welcome to the Expanded Basic Chatbot! ---
Type 'bye' or 'quit' to end the conversation.

You: Hello
Chatbot: Hey!

You: How are you?
Chatbot: I'm doing great, thanks for asking!

You: Tell me a joke
Chatbot: Why don't scientists trust atoms? Because they make up everything!

You: Bye
Chatbot: Goodbye!
```

## Customization

You can expand this chatbot by:

* Adding more `elif` branches for custom topics.
* Integrating APIs for weather, time, or news.
* Logging conversations to a file.
* Adding GUI using `tkinter` or web UI with `Flask`.

---

Created as a beginner-friendly Python chatbot to demonstrate how conversational interfaces can be built using simple control flow and text processing.
