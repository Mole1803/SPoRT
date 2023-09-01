from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/isAlive')
def hello_world():
    return jsonify({'isAlive': True})


if __name__ == '__main__':
    app.run()
