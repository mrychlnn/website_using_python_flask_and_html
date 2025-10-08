from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/uppercase', methods=['GET', 'POST'])
def uppercase():
    result = None
    if request.method == 'POST':
        input_str = request.form['inputString']
        result = input_str.upper()
    return render_template('uppercase.html', title="Uppercase Converter", result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        radius = float(request.form['radius'])
        area = math.pi * radius ** 2
    return render_template('circle.html', title="Circle Area", area=area)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        area = 0.5 * base * height
    return render_template('triangle.html', title="Triangle Area", area=area)

@app.route('/profile')
def profile():
    return render_template('profile.html', title="Profile")

@app.route('/works')
def works():
    return render_template('works.html', title='My Works')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return render_template('contact.html', title="Contact", success=True, name=name)
    return render_template('contact.html', title="Contact", success=False)

if __name__ == '__main__':
    app.run(debug=True)
