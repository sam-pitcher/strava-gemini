from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api/hello', methods=['POST'])
def hello():
    data = request.get_json()
    return jsonify({"message": "Hello, " + data.get('name', 'World')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
