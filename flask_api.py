from flask import Flask, request, jsonify, send_file, redirect, abort
from flask_swagger_ui import get_swaggerui_blueprint
from typing import List

from main import main_app

app = Flask(__name__)


@app.route('/')
def hello():
    return redirect('/docs')


@app.route('/api/test-mdm.yaml')
def swagger_yaml():
    return send_file('docs/flask_api.yaml', cache_timeout=-1)


@app.route('/app')
def queries():
    queries_array: List[str] = request.args.getlist('query')
    if not queries_array:
        abort(400, 'Must pass one or multiple \"query\" parameters')
    try:
        result = main_app(queries_array)
        return jsonify(result)
    except Exception as e:
        abort(500, str(e))


swaggerui_blueprint = get_swaggerui_blueprint(
    base_url='/docs',
    api_url='/api/test-mdm.yaml',
    config={'app_name': 'StringCounter documentation'}
)
app.register_blueprint(swaggerui_blueprint)
