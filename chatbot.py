import random

responses = {
    "hello": "Hi there!",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "hi": "Hello!",
    "hey": "Hey!",
    "what's your name": "I'm just a chatbot, so I don't have a name.",
    "who created you": "I was created by a developer.",
    "bye": "Goodbye! Feel free to come back anytime.",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "help": "Sure, how can I assist you?",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what's the weather like": "I'm sorry, I don't have access to real-time weather information.",
    "tell me a fun fact": "Did you know that honey never spoils?",
    "who won the last World Series": "I'm sorry, I don't have access to real-time sports information.",
    "tell me a story": "Once upon a time, in a land far, far away...",
    "do you like pizza": "I don't eat, but I've heard pizza is quite popular!",
    "what's the meaning of life": "The meaning of life is a philosophical question that has puzzled humans for centuries.",
    "how old are you": "I don't age, so I'm forever young!",
    "are you a robot": "I'm a chatbot, which is a type of AI program.",
    "can you sing a song": "I'm not equipped to sing, but I can provide song lyrics!",
    "default": "I'm sorry, I don't understand that."
}

# Function to generate responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    return "I'm not sure how to respond to that. Can you please rephrase your question?"

# Main conversation loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)