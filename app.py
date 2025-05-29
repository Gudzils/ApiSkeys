from flask import Flask, jsonify
import random

app = Flask(__name__)

# Хранилище ключей
api_keys = set()

# Главная страница API
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello Friend"})

# Генерация нового ключа
@app.route('/api/generate', methods=['GET'])
def generate_key():
    key = "KeyGls" + ''.join(str(random.randint(0, 9)) for _ in range(8))
    api_keys.add(key)
    return jsonify({"api_key": key})

# Проверка ключа (передается в URL)
@app.route('/api/check/<string:key>', methods=['GET'])
def check_key(key):
    # Проверяем, что ключ есть в api_keys и начинается с "KeyGls"
    if key in api_keys and key.startswith("KeyGls"):
        return jsonify({"status": "valid"})
    else:
        return jsonify({"status": "invalid"}), 401

if __name__ == '__main__':
    app.run(debug=True)
