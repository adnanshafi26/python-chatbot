print("🤖 ChatBot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Greetings
    if user_input in ["hi", "hello", "hey", "good morning", "good evening"]:
        print("🤖 ChatBot: Hi there! How’s your day going?")
    
    # Feelings
    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm doing great! Thanks for asking. How about you?")
    elif "i am fine" in user_input or "i am good" in user_input:
        print("🤖 ChatBot: That’s awesome! Keep smiling 😄")
    elif "i am sad" in user_input or "not good" in user_input:
        print("🤖 ChatBot: Oh no! 😢 Remember, tough times never last, but tough people do.")
    
    # Personal Info
    elif "your name" in user_input:
        print("🤖 ChatBot: My name is PyBot. I’m here to chat with you.")
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip().title()
        print(f"🤖 ChatBot: Nice to meet you, {name}! 😄")
    
    # Fun Facts
    elif "joke" in user_input:
        print("🤖 ChatBot: Why don’t skeletons fight each other? Because they don’t have the guts! 😂")
    elif "fact" in user_input:
        print("🤖 ChatBot: Did you know? Honey never spoils! Archaeologists found 3000-year-old honey still edible.")
    
    # Time & Date
    elif "time" in user_input:
        from datetime import datetime
        print(f"🤖 ChatBot: The current time is {datetime.now().strftime('%H:%M:%S')}.")
    elif "date" in user_input:
        from datetime import datetime
        print(f"🤖 ChatBot: Today’s date is {datetime.now().strftime('%Y-%m-%d')}.")
    
    # Hobbies
    elif "what do you do" in user_input or "purpose" in user_input:
        print("🤖 ChatBot: I love chatting and helping people with their questions.")
    elif "your hobby" in user_input:
        print("🤖 ChatBot: My hobby is talking to you all day long! 💬")
    
    # Goodbye
    elif user_input in ["bye", "exit", "quit", "see you"]:
        print("🤖 ChatBot: Goodbye! Have a great day ahead! 👋")
        break
    
    # Default
    else:
        print("🤖 ChatBot: Hmm, I didn’t quite get that. Could you rephrase? 🤔")
