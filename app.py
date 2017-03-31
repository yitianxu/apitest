#!flask/bin/python
from flask import Flask, jsonify
from flask import request 


app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    }
]

tasks_2 = [
    {
        'id': 3,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 4,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]



@app.route('/todo/api/v1.0/countries', methods=['GET'])
def target(): 
    if 'target' in request.args:        
        if request.args['target'] == 'source':            
            return jsonify({'tasks': tasks})
        elif request.args['target'] == 'destination': 
            return jsonify({'tasks_2':tasks_2})
        else:
            return request.args['error enquries'] 



@app.route('/todo/api/v1.0/hello', methods=['GET'])
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe' 



@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)