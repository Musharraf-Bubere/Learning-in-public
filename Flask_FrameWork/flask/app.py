from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSI (We Server Gateway Interface) application.
'''

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course, This should be an amazing course."

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__=="__main__":  # Run this code only when this file is executed directly, not when it’s imported.
    app.run(debug=True)