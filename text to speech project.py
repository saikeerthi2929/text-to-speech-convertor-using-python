# import the pyttsx module inside program
import pyttsx3

# initializing the module
engine = pyttsx3.init()

# .say() function is used to speak the text you have written 
# inside the function
engine.say("hey this is the text to speech converter  created by keerthi")
engine.say("please enter the text you want ")
engine.say("i will convert that into voice ")
engine.say("a basic project created by me so that i can use it for fun")
engine.say("just kidding ")
# this is used to process and run the program commands
engine.runAndWait()