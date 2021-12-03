from flask import Flask, render_template, jsonify, request
from flask.wrappers import Response
import trainedmodel
import speech_recognition as sr
import subprocess
import webbrowser
import pyttsx3
import time
import os
from threading import Thread
import pandas as pd
from gtts import gTTS, tts
from requests import post
from random import choice
from os import remove, system

app = Flask(__name__)

df = pd.read_csv('files/csv_file/guide.csv')

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question'].lower()
        if the_question == "software engineer".lower():
            response = df.iloc[0,2]
        elif the_question == "Data Science".lower():
            response = df.iloc[1,2]
        elif the_question == "Data Analyst".lower():
            response = df.iloc[2,2]
        else:
            response =trainedmodel.chatbot_response(the_question)
            tts = gTTS(response)
            tts.save('files/temp_audio/response.wav')
    return jsonify({"response": response })
   

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
