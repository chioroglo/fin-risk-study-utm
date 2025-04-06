import os
from dotenv import load_dotenv
from flask import Flask, Response, jsonify, request
from flask_basicauth import BasicAuth

load_dotenv()
app = Flask(__name__, static_folder='/wwwroot')
app.config['BASIC_AUTH_USERNAME']= os.getenv('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')
basic_auth = BasicAuth(app)

@app.route('/health/api', methods=['GET'])
@basic_auth.required
def health_check_api():
    return Response(response="<b>API is healthy!</b>",
                    status=200,
                    mimetype='text/html')
