from flask import Flask, Response, render_template, request, redirect, url_for, flash
from groot import app


@app.route("/")
@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')
        

@app.route("/register", methods=['POST', 'GET'])
def register():
    return render_template('register.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('index.html', title='Dashboard')


@app.route('/policies', methods=['GET', 'POST'])
def policies():
    return render_template('policies.html', title='Policies')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html', title='Profile')


@app.route('/sensors', methods=['GET', 'POST'])
def sensors():
    return render_template('sensors.html', title='Sensors')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
	