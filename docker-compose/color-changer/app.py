from os import environ
from flask import Flask, render_template, request, make_response, jsonify
from flask_restful import reqparse

app = Flask(__name__)
color = ""


@app.route('/')
def index():
    content = make_response(render_template('index.html'))
    return content


@app.route('/_ajaxAutoRefresh', methods= ['GET'])
def stuff():
    return jsonify(color=color)


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


@app.route('/change-color', methods=['PUT'])
def change_color():
    global color
    request.get_json(force=True)

    parser = reqparse.RequestParser()
    parser.add_argument('color', required=True)
    args = parser.parse_args()

    color = (args['color'])
    
    print("Changing color to", color)
    
    returnData = "Command accepted"

    return returnData, 201
    
@app.route('/read-color', methods=['GET'])
def read_color():
    global color
    
    print("Reading color")
    
    returnData = color
    
    return returnData, 201


if __name__ == "__main__":
	app.run(debug=eval(environ.get("DEBUG", "True")), \
                host='0.0.0.0', \
                port=int(environ.get('PORT', '5000')), threaded=True)
