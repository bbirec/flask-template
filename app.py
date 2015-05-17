from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)
app.config.from_object('config.Config')

# Routes
@app.route('/')
def home():
	app.logger.info('Home')
	return render_template('home.html', name='Heehong')

@app.route('/api/greeting')
def sample_json():
	out = 'Hello ' + request.args.get('name', '')
	return jsonify(output=out)

@app.route('/error')
def sample_error():
	raise Exception("Can't connect to database")

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	return render_template('500.html'), 500

# For debug
if __name__ == '__main__':
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0', port=port)