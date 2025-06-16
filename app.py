from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

API_KEY = 'your-api-key'    # 输入你自己Dify的API_KEY
API_URL = 'your-api-url'    # 输入你自己的API_URL

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    theme = data.get('theme')
    count = data.get('count')

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    workflow_data = {
        "inputs": {
            "theme": theme,
            "count": count
        },
        "response_mode": "blocking",
        "user": "web-user"
    }

    response = requests.post(API_URL, json=workflow_data, headers=headers)

    if response.status_code == 200:
        res = response.json()
        html = res['data']['outputs']['output']
        return jsonify({"html": html})
    else:
        return jsonify({"error": "生成失败"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 