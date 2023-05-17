
# to isntall "pip install pywhatkit"

import pywhatkit as pwk

# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     pwk.sendwhatmsg("+91XXXXXX5980", "Hi, how are you?", 20, 34)

     print("Message Sent!") #Prints success message in console

     # error message
except: 
     print("Error in sending the message")

     