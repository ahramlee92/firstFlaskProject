from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') # url that navigate through html code. Called route or views
@app.route('/home')
def home_page():
    return render_template('home.html')
