from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "API Flask DevSecOps"})


@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "flask_app"})


@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"data": [1, 2, 3, 4, 5]})


@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"received": data, "status": "created"}), 201


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
