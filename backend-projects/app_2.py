from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)

def get_locale():
	return request.accept_languages.best_match(['en', 'es', 'fr'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
	locale = get_locale()
	return render_template('index.html', locale=locale)


if __name__ == '__main__':
	app.run(debug=True)
