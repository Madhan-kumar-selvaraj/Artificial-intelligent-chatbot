# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:59:57 2020

@author: Madhan Kumar Selvaraj
"""

from flask import Flask, render_template, request
from chatbot_model import chatbot_response
from scrape import scrape_data


check_wikipedia1 = ['what', 'is']
check_wikipedia2 = ['who', 'is']
check_wikihow = ['how', 'to']

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_request = request.args.get('msg')  # Fetching input from the user
    user_request = user_request.lower()
    if len(user_request.split(" ")) > 1:
        check_search = user_request.split(" ")[0]
        if check_search == 'google':
            user_request = user_request.replace("google","")
            user_request = user_request.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
            check_query = user_request.split(" ")[1]
            check_text = user_request.split(" ")[1:3]
            if check_text == check_wikipedia1 or check_text == check_wikipedia2:
                response = scrape_data(user_request, "wikipedia")
            elif check_text == check_wikihow:
                response = scrape_data(user_request, "wikihow")
            elif check_query == "nearby":
                response = scrape_data(user_request, "nearby")
            else:
                response = scrape_data(user_request, "")
                
        else:
            response = chatbot_response(user_request)                

    else:
        response = chatbot_response(user_request)
    
    return response

if __name__ == "__main__":
    app.run(threaded=False)