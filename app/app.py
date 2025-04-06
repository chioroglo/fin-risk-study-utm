import os
from dotenv import load_dotenv
from flask import Flask, Response, jsonify, request
from flask_basicauth import BasicAuth
from flask_cors import CORS
from pydantic import ValidationError

from service.financial_risk_model_service import FinancialRiskModelService
from model.financial_risk_response import FinancialRiskResponse
from model.financial_risk_model import FinancialRiskModel

load_dotenv()
app = Flask(__name__, static_folder='/wwwroot')
CORS(app)
app.config['BASIC_AUTH_USERNAME']= os.getenv('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')
basic_auth = BasicAuth(app)

@app.route('/health/api', methods=['GET'])
@basic_auth.required
def health_check_api():
    return Response(response="<b>API is healthy!</b>",
                    status=200,
                    mimetype='text/html')

@app.route('/calculate-audit', methods=['POST'])
@basic_auth.required
def calculate_risk_category():
    try:
        body = request.get_json()
        input_data = FinancialRiskModel(**body)
        print(input_data.dict())
        model_service = FinancialRiskModelService()
        response = model_service.predict_audit_effectiveness_score(input_data)
        response = FinancialRiskResponse(**{ "audit_effectiveness_score": response[0] })
        return jsonify(response.model_dump_json())
    except ValidationError as e:
        return jsonify({ "error": e.errors() }), 400

    # payload = request.get_json()
    # request_model = MlModelService.from_dict(payload)
    # category = MlModelService().get_category(request_model)

    # return jsonify({
    #     'result' : category
    # })