from flask import Flask, jsonify, abort, request
...
app = Flask(__name__)
...
@app.route('/')
@app.route('/foo', methods=['GET'])
def foo():
    return "bar2!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)