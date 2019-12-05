from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

if __name__ == "__main__":
	app.run(debug=True)