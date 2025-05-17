from flask import Flask, jsonify, Response
from typing import Dict, Any
import requests
import sys

app: Flask = Flask(__name__)

@app.route('/fetch-data', methods=['GET'])
def fetch_data() -> Response:
    response: requests.Response = requests.get('https://ipinfo.io')
    data: Dict[str, Any] = response.json()

    modified_data: Dict[str, Any] = {
        'original': data,
        'message': 'Data fetched and modified successfully'
    }

    return jsonify(modified_data)

@app.route('/dummy', methods=['GET'])
def dummy() -> Response:
    return 42

def main() -> None:
    from gunicorn.app.wsgiapp import run
    sys.argv = ['gunicorn', '-w', '4', '-b', '[::]:3001', 'grafonix:app']
    run()

if __name__ == '__main__':
    main()
