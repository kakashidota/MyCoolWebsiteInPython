import gspread
from flask import Flask, render_template, request

gc = gspread.service_account(filename='tillvadsomhelst.json')
sh = gc.open('flask-website')

shProfile = sh.get_worksheet(0)
shContacts = sh.get_worksheet(1)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        shContacts.append_row([request.form['name'], request.form['email'], request.form['message']])


    profile = {
        'about': shProfile.acell('B1').value,
        'interests': shProfile.acell('B2').value,
        'experience': shProfile.acell('B3').value,
        'education': shProfile.acell('B4').value
    }
    return render_template('index.html', profile=profile)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template('contact.html')
