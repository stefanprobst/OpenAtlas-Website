# Created by Alexander Watzinger and others. Please see README.md for licensing information
from flask import Flask, request

try:
    import mod_wsgi
except ImportError:
    mod_wsgi = None

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')  # Load config
app.config.from_pyfile('production.py')  # Load instance

from openatlas_website.util import filters
from openatlas_website.views import index, team, projects


@app.before_request
def before_request():
    if request.path.startswith('/static'):  # pragma: no cover
        return  # Only needed if not running with apache and static alias


@app.after_request
def apply_caching(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'

    # Todo: activate Content-Security-Policy after removal of every inline CSS and JavaScript
    # response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response


app.register_blueprint(filters.blueprint)


if __name__ == "__main__":  # pragma: no cover
    app.run()
