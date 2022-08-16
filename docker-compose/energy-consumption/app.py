from os import environ
from flask import Flask, render_template, request, make_response, jsonify
from flask_restful import reqparse
import json

app = Flask(__name__)
energy = ""


@app.route('/')
def index():
    content = make_response(render_template('index.html'))
    return content


@app.route('/_ajaxAutoRefresh', methods= ['GET'])
def stuff():
    return jsonify(energy=energy)


@app.route('/register', methods=['POST'])
def register():
    request.get_json(force=True)

    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True)
    args = parser.parse_args()

    id = args['id']

    print("Registering device: ", id)

    returnData = "Device registered"

    return returnData, 201


@app.route('/change-logs', methods=['PUT'])
def change_logs():
    global energy
    request.get_json(force=True)

    parser = reqparse.RequestParser()
    parser.add_argument('energy', required=True)
    args = parser.parse_args()

    energy = (args['energy'])
    
    print("Changing energy to", energy)
    
    returnData = "Command accepted"

    return returnData, 201
    
@app.route('/check-consumption', methods=['GET'])
def check_consumption():
    with open('logData.json', 'r') as f:
        data = json.load(f)
    
    returnData = "Energy consumed last week in total for all devices is " + str(data["totalWeek"]) + " W, and from beggining of this month consumption until now totals " + str(data["totalMonth"]) + " W."
    
    return returnData, 201


if __name__ == "__main__":
	app.run(debug=eval(environ.get("DEBUG", "True")), \
                host='0.0.0.0', \
                port=int(environ.get('PORT', '5000')), threaded=True)
