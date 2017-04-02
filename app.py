#!flask/bin/python
from flask import Flask, jsonify, render_template
from flask import request 

import random

app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify( { 'error': 'bad query' } ), 500)

# task list  
# it can query for db  
tasks = [
      {"name": "United Kingdom", "isoCode": "GB"}, 
      {"name": "Ireland", "isoCode": "IE"}
]

# destination list
# it can query for db  
tasks_2 = [
      {"name": "Spain", "isoCode": "ES"}, 
      {"name": "France", "isoCode": "FR"}
]


# api interface to get country information 
@app.route('/todo/api/v1.0/countries', methods=['GET'])
def target(): 
    if 'target' in request.args:        
        if request.args['target'] == 'source':            
            return jsonify({'tasks': tasks})
        elif request.args['target'] == 'destination': 
            return jsonify({'tasks_2':tasks_2})
        else:
            return request.args['error enquries'] 


# hello world testing 
#@app.route('/todo/api/v1.0/hello', methods=['GET'])
#def api_hello():
#        return 'Hello world' 


@app.route('/')
def index():
    return 'default page: /todo/api/v1.0/countries?target=source or /todo/api/v1.0/countries?target=destination'


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0")