from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [{"object": "Bust a move.", "DUNZO!": False}] 

@app.route("/todos", methods = ["GET"])
def get_todos(): 
    return jsonify(todos)

@app.route("/todos", methods = ["POST"])
def post_todos():
    request_body = request.get_json(force = True)
    todos.append((request_body))
    return jsonify(todos)

@app.route("/todos/<int:position>",methods = ["DELETE"])
def delete_todos(position):
    todos.pop(position)
    return jsonify

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)