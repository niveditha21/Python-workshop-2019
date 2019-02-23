from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return"Hello..!!"
@app.route("/home")
def home():
    return"My home page"
@app.route("/contact")
def contact():
    return"My contact"
if(__name__=="__main__"):
    app.run()