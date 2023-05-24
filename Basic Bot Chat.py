import random

reply = {
    "hello": ["Hello!", "Hi there!", "Greetings!","Hi"],
    "how are you": ["I'm good, thanks! and  How Are you", "I'm doing great! and you", "All is well! and you"],
    "bye": ["Goodbye!", "Farewell!", "See you later!"],
    "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm still learning!"],
}

def bot_reply(User):
    User = User.lower()

    for i in reply:
        if i in User:
            return random.choice(reply[i])
        
    return random.choice(reply['default'])

while True:
    Question = input('User: ')
    Answer = bot_reply(Question)
    print(f'Bot: {Answer}')
