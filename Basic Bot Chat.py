import random

# Define a dictionary of possible bot responses
reply = {
    "hello": ["Hello!", "Hi there!", "Greetings!","Hi"],
    "how are you": ["I'm good, thanks! and  How Are you", "I'm doing great! and you", "All is well! and you"],
    "bye": ["Goodbye!", "Farewell!", "See you later!"],
    "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm still learning!"],
}
# Define a function to generate a bot response
def bot_reply(User):
    # Convert user input to lowercase
    User = User.lower()

    # Check if the user input matches any predefined key in the responses dictionary
    for i in reply:
        if i in User:
            # Randomly select a response from the list of possible responses
            return random.choice(reply[i])
        # If no match is found, return a default response
    return random.choice(reply['default'])

# Chat loop
while True:
    Question = input('User: ')
    Answer = bot_reply(Question)
    print(f'Bot: {Answer}')
