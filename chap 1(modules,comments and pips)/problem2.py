# A module is simply a file containing Python code. It can define functions, classes, and variables, 
# and it can also include runnable code.simple we can say it that we can use code of any other person
# pip stands for "Pip Installs Packages". It's the Python package manager used to install and manage third-party libraries (modules) from the Python Package Index (PyPI).
# using external module
import pyjokes
jokes=pyjokes.get_joke()
print(jokes)
# another module
import pyttsx3
engine = pyttsx3.init()
engine.say("i am a good boy")
engine.runAndWait()