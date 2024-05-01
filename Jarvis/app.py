# from flask import Flask, request, jsonify,render_template
# import jarvis

# app = Flask(__name__)

# @app.route("/")
# def landing():
#     return render_template("index.html")

# @app.route("/hello")
# def hello():
#     return "hello"
 
# @app.route('/jarvis/time', methods=['POST'])
# def get_time():
#     from jarvis import time
    
#     # Call your time function from your Jarvis code here (e.g., time())
#     # Extract the time as a string
#     time_string = time()#"Current time is..."  # Replace with actual time retrieval
#     return jsonify({'time': time_string})

# # Similar routes for other functionalities (date, wikipedia search, etc.)

# if __name__ == '__main__':
#     app.run(debug=False)

from flask import Flask, request, jsonify
import pyttsx3
import datetime
import speech_recognition as sr
import os
import random

app = Flask(__name__)
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

@app.route('/time', methods=['GET'])
def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    return jsonify({"time": Time})

@app.route('/date', methods=['GET'])
def get_date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    return jsonify({"date": f"{day}/{month}/{year}"})

@app.route('/talk', methods=['GET'])
def talk_to_jarvis():
    query = request.args.get('query')
    # Implement Jarvis functions here similar to your script
    return jsonify({"response": "Processed your query"})

if __name__ == "__main__":
    app.run(debug=False)