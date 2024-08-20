api= "AIzaSyAt0dlVOUXINcIXJ_eR2RoRj6nOPxaby-8"


import google.generativeai as palm
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}
# render_template renders the html template & return them as a response
# request handles the incoming request (like the prompt)
from flask import Flask, render_template, request

# this creates the web application - initialising the process
app = Flask(__name__)

# @app.route gets the root URL: http://localhost:5000/
# GET: request data, POST: submit data
@app.route("/", methods = ["GET","POST"])
# this function is called whenever someone visits the root URL of http://localhost:5000/ 
def index():
    # access the front-end specifics
    return(render_template("index_tut_week2.html"))

@app.route("/financial_QA", methods = ["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite", methods = ["GET","POST"])
def makersuite():
    #get info from front end to back end using request
    q = request.form.get("q")
    r = palm.chat(prompt = q, **model)
    return(render_template("makersuite.html", r= r.last))

@app.route("/prediction", methods = ["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

# this runs the web application 
if __name__ == "__main__":
    app.run()
