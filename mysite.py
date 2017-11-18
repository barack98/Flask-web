from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return ("<h2>Welcome to mysite<h2>")

@app.route('/profile/<username>')
def profile(username):
	return 'Hey %s' % username

@app.route('/post/<int:post_id>')
def post(post_id):
	return 'This post is No: %s ' % post_id