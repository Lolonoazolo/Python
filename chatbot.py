# A Rule based AI chat bot

import datetime
import time

name=input("Swagat hai , Please enter your name")
presenthour = datetime.datetime.now().hour
if 5<= presenthour <=11:
  print("Good Morning ,",name)
elif 12<= presenthour <=16:
  print("Good Afternoon ,",name)
elif 17<= presenthour <=21:
  print("Good Evening ,",name)
else:
  print("Good Night")

print("You can ask me any question")
print ("Type 'bye' to exit the chat")

#chatbot memory 

responses ={
  "hello" : "Hi , Welcome . How can I help You",
  "how are you" : "I am good , Thank you",
  "what is your name" : "I am a chatbot created by AI",
  "motivate me" : "Keep going , Every bug of your project makes you a better coder",
  "what can you do" : "I can answer your questions",
  "bye" : "Goodbye , Have a great day"  
}

def getresponsebot (user_input):
  user_input = user_input.lower()
  for eachkey in responses :
    if eachkey in user_input :
      return responses[eachkey]

  return "I am not table to tell that yet"

# take user input
while True :  
  user_input = input("please as your question : ")
  reply = getresponsebot(user_input)
  print("bot response :  ", reply)

  if "bye" in user_input.lower():
     break 