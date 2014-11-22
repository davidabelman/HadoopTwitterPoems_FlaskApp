from flask import Flask, render_template, request
from flask.ext.script import Manager

app = Flask(__name__)
app.debug = True
manager = Manager(app)

@app.route('/')
def home():
	"""
	Show main page
	Javascript on this page takes care of all navigation
	"""
	print "Loading main.html"
	return render_template('main.html')

@app.route('/poem/<poem_name>')
def poem(poem_name):
	"""
	Show poem page
	A poem is loaded from external module
	Lines of poem (containing username, date, twitter_id as well as poem text) are looped through within jinja template
	"""	
	print "Loading %s poem" %poem_name
	poem = poem_name.lower().strip()
	
	# This code imports the poem without refering to it by name (e.g. from obama import title, poem, desc)
	module = __import__(poem)
	title = module.title
	poem = module.poem
	desc = module.desc

	# Parse the poem
	lines = poem.split('\n')
	poem_split = [line.split('\t') for line in lines if line]

	# Send poem title, desc and lines (which include username, date etc.) to jinja
	return render_template('poem.html', title=title, desc=desc, poem=poem_split)

if __name__ == '__main__':
	manager.run()

