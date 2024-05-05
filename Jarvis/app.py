# from flask import Flask, request, jsonify,render_template
# import jarvis

# app = Flask(__name__)

# @app.route("/")
# def landing():   
#     return render_template("index.html")

# # @app.route("")

# @app.route('/jarvis/time', methods=['POST'])
# def get_time():
#     from jarvis import time
    
#     # Call your time function from your Jarvis code here (e.g., time())
#     # Extract the time as a string
#     time_string = time()#"Current time is..."  # Replace with actual time retrieval
#     return jsonify({'time': time_string})

# # Similar routes for other functionalities (date, wikipedia search, etc.)

# if __name__ == '__main__':
#     app.run(host="0.0.0.0")

from flask import Flask, render_template, request, jsonify
import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import random
import pyautogui
import time


app = Flask(__name__)



def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    

def time1():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))
    
# def screenshot():
#     img = pyautogui.screenshot()
#     img_path = os.path.expanduser("~\\Pictures\\ss.png")
#     img.save(img_path)

def wishme():
    # print("Welcome back sir!!")
    # speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir")

    speak("please tell me how may I help you.")
    print("please tell me how may I help you.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        query=query.lower()
        if query.endswith("jarvis"):
          print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"
    if query.endswith("jarvis"):
      return query
    else:
        return ""

@app.route('/')
def index():
    wishme()
    return render_template('index.html')

@app.route('/process_voice_command', methods=['POST'])
def process_voice_command():
    data = request.json
    voice_command = data.get('voice_command') 
    voice_command=voice_command.lower()  
    response = process_command(voice_command)
    return jsonify({'response': response})

def process_command(command):
    if "time" in command:
        time1()
        
    elif "date" in command:
        date()
        return "Displayed date"
    elif "who are you" in command:
        speak("I'm JARVIS and I'm a desktop voice assistant.")
        print("I'm JARVIS and I'm a desktop voice assistant.")
        return "I'm JARVIS and I'm a desktop voice assistant."
    elif "how are you" in command:
        speak("I'm fine sir, What about you?")
        print("I'm fine sir, What about you?")
        return "I'm fine sir, What about you?"
    elif "fine" in command or "good" in command:
        speak("Glad to hear that sir!!")
        print("Glad to hear that sir!!")
        return "Glad to hear that sir!!"
    elif "tell me something" in command:
        try:
            speak("Ok wait sir, I'm searching...")
            command = command.replace("tell me something","")
            result = wikipedia.summary(command, sentences=2)
            print(result)
            speak(result)
            return result
        except:
            speak("Can't find this page sir, please ask something else")
            return "Can't find this page sir, please ask something else"
        
    # elif "open youtube" in command:
    #     wb.open("https://www.youtube.com/")
    #     speak("Opening YouTube")
    #     return "Opened YouTube"

    # elif "open google" in command:
    #     speak("opening google")
    #     wb.open("google.com") 
    #     return "Opened Google"
    # elif "open stack overflow" in command:
    #     speak("opening stackoverflow")
    #     wb.open("stackoverflow.com")
    #     return "Opened Stack Overflow"
    elif command.startswith("open"):
        speak(f"opening{command[5:]}")
        wb.open(command[5:] + ".com")
        return "Opened " + command[5:] + ".com"
    
    # elif "play music" in command:
    #     song_dir = os.path.expanduser("C:\\Users\\vaibh\\Music")
    #     songs = os.listdir(song_dir)
    #     x = len(songs)
    #     y = random.randint(0,x)
    #     os.startfile(os.path.join(song_dir, songs[y]))
    #     return "Playing music"
    elif "play music" in command:
        song_dir = "C:\\Users\\vaibh\\Music"
        songs = [file for file in os.listdir(song_dir) if file.lower().endswith(('.mp3', '.wav', '.ogg'))]
        if not songs:
            speak("No files found")
            return "No music files found"
        
        random_song = random.choice(songs)
        song_path = os.path.join(song_dir, random_song)
        try:
            os.startfile(song_path)
            speak(random_song)
            return f"Playing music: {random_song}"
        except Exception as e:
            return f"Error playing music: {str(e)}"
        
    
    elif "start chrome" in command:
        try:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening Chrome")
            os.startfile(chromePath)
            return "Started Chrome"
        except Exception as e:
            speak("File location not found")
            print("File location not found")
            return "File location not found"
    elif "search on chrome" in command:
        try:
            # speak("What should I search?")
            # search_query = takecommand()
            command=command[17:]
            wb.open_new_tab(command)
            print(command)
            return "Searching on Chrome: " + command
        except Exception as e:
            speak("Can't open now, please try again later.")
            print("Can't open now, please try again later.")
            return "Can't open now, please try again later."
    elif "just remember" in command:
        speak("What should I remember")
        data = takecommand()
        speak("You said me to remember that" + data)
        print("You said me to remember that " + str(data))
        remember = open("data.txt", "w")
        remember.write(data)
        remember.close()
        return "Remembered: " + data
    elif "do you remember anything" in command:
        remember = open("data.txt", "r")
        speak("You told me to remember that" + remember.read())
        print("You told me to remember that " + str(remember))
        return "You told me to remember that" + remember.read()
    # elif "screenshot" in command:
    #     screenshot()
    #     speak("I've taken screenshot, please check it")
    #     return "Screenshot taken"
    elif "offline" in command:
        quit()
        return "Shutting down"

# if __name__ == '__main__':
#     app.run(debug=True)