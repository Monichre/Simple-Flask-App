from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return   "Hello World"

@app.route('/about')
def about():
    return "This is the muh fuckin about page"

@app.route('/contact')
def contact():
    return "Contact me yo"


app.run(debug=True)
