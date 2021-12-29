import sys
from pathlib import Path
sys.path.insert(0, '/usr/lib/python3/dist-packages/')  # For GitHub actions
from flask import Flask, Response, request

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')  # type: ignore

if (Path(app.root_path).parent / 'instance' / 'production.py').is_file():
    app.config.from_pyfile('production.py')  # pragma: no cover

from openatlas_website.util import filters
from openatlas_website import views


@app.before_request
def before_request() -> None:
    if request.path.startswith('/static'):  # pragma: no cover
        return  # Only needed if not running with apache and static alias


@app.after_request
def apply_caching(response: Response) -> Response:
    response.headers['Strict-Transport-Security'] = \
        'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


if __name__ == "__main__":  # pragma: no cover
    app.run()
