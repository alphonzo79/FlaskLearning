from flask import Flask
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def index():
	return "Hello, World!"

@app.route('/second')
def the_time():
	cur_time = str(datetime.now())
	return cur_time + " is the current time"

if __name__ == '__main__':
	app.run(port=5000, debug=True)
