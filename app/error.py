from flask import render_template
from app import app

@app.errorhandler(404)
def fourOwfour(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOWfour.html'),404