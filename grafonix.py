from flask import Flask, jsonify
import requests
import sys

app = Flask(__name__)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    response = requests.get('https://ipinfo.io')
    data = response.json()

    modified_data = {
        'original': data,
        'message': 'Data fetched and modified successfully'
    }

    return jsonify(modified_data)

def main():
    from gunicorn.app.wsgiapp import run
    sys.argv = ['gunicorn', '-w', '4', '-b', '[::]:3001', 'grafonix:app']
    run()

if __name__ == '__main__':
    main()
