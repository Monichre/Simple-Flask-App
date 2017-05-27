from flask import Flask
from flask import render_template
# from flask import request # -- We can also lose this as well


app = Flask(__name__)


# -- Here we are adding routes to a function we've called index -- literally only because its the landing page -- It's actually a view
# -- You can add multiple routes to a function so that your application becomes more complex and so the function performs consistently

@app.route('/')
@app.route('/<name>') # -- This line tells flask to capture anything that comes after the initial forward slash -- in this case 'name'
def index():
    # name = request.args.get('name', name) # -- Therefore we can actually get rid of this line to clean up the code
    return   render_template("index.html")

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    # return '{} + {} = {}'.format(num1, num2, num1 * num2)
    return render_template("add.html", num1 = num1, num2 = num2)

@app.route('/about')
def about():
    return "This is the muh fuckin about page"

@app.route('/contact')
def contact():
    return "Contact me yo"


app.run(debug=True)
