from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.balance_editor import balance_editor_composer

from src.main.middlewares.auth_jwt import auth_jwt_verify

bank_routes_bp = Blueprint("bank_routes", __name__)

@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    http_request = HttpRequest(body=request.json) # Pegando informações do Body
    http_response = user_register_composer().handle(http_request) # Chamando o método handle do UserRegisterView
    return jsonify(http_response.body), http_response.status_code # Retornando o body e o status code

@bank_routes_bp.route("/bank/login", methods=["POST"])
def create_login():
    http_request = HttpRequest(body=request.json)
    http_response = login_creator_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"]) # PATCH = quando você quer atualizar um recurso dentro do servidor
def edit_balance(user_id):
    token_information = auth_jwt_verify()
    http_request = HttpRequest(
        body=request.json, 
        params={"user_id": user_id},
        token_infos=token_information # Passando o token_information para o HttpRequest
        )
    
    http_response = balance_editor_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code
    