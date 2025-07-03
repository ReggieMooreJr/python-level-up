from flask import Flask, render_template, request
from readings import get_rotated_readings
# This line is the APP Name#
app = Flask(__name__)
#vsets up the routing for APIS #
@app.route('/', methods=['GET', 'POST'])
#This subroutine takes input from the user and then renders it back to them #
def index():
    rotated_readings = []
    if request.method == 'POST':
        try:
            offset = int(request.form['number'])
            rotated_readings = get_rotated_readings(offset)
        except ValueError:
            rotated_readings = ["Invalid number entered."]
    return render_template('index.html', readings=rotated_readings)
def translate ():
    # Check if the user selected Spanish in the form
    rotated_readings_spanish = []
    if request.form.get('language') == 'spanish':
        try:
            offset_sp = int(request.form['number'])
            rotated_readings_spanish = get_rotated_readings(offset_sp, language='spanish')
        except ValueError:
            rotated_readings_spanish = ["Número inválido ingresado."]
    return render_template('index.html', readings=rotated_readings_spanish)

