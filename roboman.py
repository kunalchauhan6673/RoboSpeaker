import time
import pyttsx3

if __name__ == '__main__':
    print("Created by Kunal Chauhan")
    engine = pyttsx3.init()  

    while True:
        x = input("What do you want me to speak: ")
        if x == "bye":
            farewell_message = "Thank you for using me! Goodbye!"
            engine.say(farewell_message)
            engine.runAndWait()
            break
        engine.say(x)
        time.sleep(0.5)  
        engine.runAndWait()