import pyttsx3
import pythoncom
friend = pyttsx3.init()
speech = input("Bir şeyler söyle: ")
friend.say(speech)
friend.runAndWait()