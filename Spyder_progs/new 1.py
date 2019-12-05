from flask import flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
	return "<h1>this is home page</h1> <p>This is the para at home</p>"
	
	
if __name__ == "__main__":
	app.run(debug=True)