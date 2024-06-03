from flask import Flask, request, render_template, redirect, url_for, session
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['SECRET_KEY'] = 'secret_key'

babel = Babel(app)

SUPPORTED_LOCALES = ['en', 'es', 'fr', 'de']

def get_locale():
	locale = request.args.get('locale')
	if locale in SUPPORTED_LOCALES:
		session['locale'] = locale
		return locale

	if 'locale' in session:
		return session['locale']

	return request.accept_languages.best_match(SUPPORTED_LOCALES)

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
	locale = get_locale()
	return render_template('index.html', locale=locale)

@app.route('/set_locale', methods=['POST'])
def set_locale():
	session['locale'] = request.form['locale']
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)

