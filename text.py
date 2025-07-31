# pip install nltk

import nltk
import re
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

pairs = [
[r"hi|hello|hey|good morning|good evening", 
     ["Hello! How can I help you today?", 
      "Hi there! How may I assist you?", 
      "Hey! What brings you here today?"]],

    # Introductions
    [r"my name is (.*)", 
     ["Hello %1! How can I assist you today?", 
      "Nice to meet you, %1. What can I do for you?"]],
    
    [r"(.*) your name?", 
     ["I am your friendly chatbot!", 
      "You can call me ChatBot. I’m here to help you!"]],

    # Feelings
    [r"how are you?", 
     ["I'm just a bot, but I'm doing well. How about you?", 
      "Doing great! Thanks for asking. How are you feeling?"]],

    [r"i am (sad|happy|angry|tired|excited)", 
     ["Why are you feeling %1?", 
      "I'm here for you. Tell me more about why you're %1."]],

    # Weather
    [r"what's the weather like(.*)?", 
     ["I can't check live weather, but it’s always sunny in my code!", 
      "I suggest checking your favorite weather app for that."]],
    
    # Time
    [r"what time is it(.*)?", 
     ["I don’t have a clock, but your system time should tell you!", 
      "I'm not sure, but it's always the right time to chat!"]],

    # Jokes
    [r"tell me a joke", 
     ["Why don't skeletons fight each other? They don't have the guts!", 
      "Why did the computer visit the doctor? Because it had a virus!"]],

    # Hobbies
    [r"i like (.*)", 
     ["That's great! I also enjoy %1 (in my own way).", 
      "Nice! How long have you been interested in %1?"]],
    
    [r"do you like (.*)", 
     ["I think %1 is quite fascinating!", 
      "I don’t have feelings, but %1 sounds cool!"]],

    # Help & Assistance
    [r"(.*) (help|assist) (.*)", 
     ["Sure! How can I assist you with %3?", 
      "Absolutely! Let’s work on %3 together."]],
    
    [r"can you help me with (.*)", 
     ["Of course! Let’s see what we can do about %1.", 
      "Happy to help with %1. Could you tell me more?"]],

    # Learning & Education
    [r"i want to learn (.*)", 
     ["Great choice! %1 is an exciting subject.", 
      "There are lots of resources for %1. Want suggestions?"]],

    [r"what is (.*)", 
     ["%1 is something I can definitely help explain.", 
      "Let me tell you more about %1."]],

    # Technology
    [r"(.*) (AI|machine learning|python|coding|technology)", 
     ["That’s a popular topic! What do you want to know about %2?", 
      "%2 is a rapidly growing field. I can provide guidance!"]],

    # Chatbot Capabilities
    [r"(.*) can you do?", 
     ["I can chat, tell jokes, answer questions, and assist with tasks!", 
      "I'm good at small talk, tech help, and more. Just ask!"]],
    
    # Career/Work
    [r"i work as a (.*)", 
     ["That’s amazing! What do you enjoy about being a %1?", 
      "Nice! Being a %1 must be quite interesting."]],

    # Motivation
    [r"i am feeling down|i feel hopeless", 
     ["I'm here for you. Want to talk about it?", 
      "It’s okay to feel this way. I'm listening."]],

    # Goodbyes
    [r"bye|exit|quit|see you", 
     ["Goodbye! Have a great day!", 
      "See you later! Come back anytime."]],

    # Fallback
    [r"(.*)", 
     ["I'm sorry, I didn't understand that. Could you rephrase?", 
      "Could you please elaborate?", 
      "That’s interesting. Tell me more."]]
]

class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
        
    def respond(self, user_input):
        return self.chat.respond(user_input)
    
    
    
def chat_with_bot():
    print("Hello, I am your chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")
        
        
        
chatbot = RuleBasedChatbot(pairs)
chat_with_bot()