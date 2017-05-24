from flask import Flask # Creates the application object

app = Flask(__name__)

from app import views #imports the views module
# Putting the import at the end of avoids a circular import error
