from flask import request
from src.drivers.jwt_handler import JWTHandler
from src.errors.types.http_unauthorized import HttpUnauthorizedError

def auth_jwt_verify():
    jwt_handle = JWTHandler()
    raw_token = request.headers.get("Authorization") # Pega o token que está no header da requisição que está chegando no servidor
    user_id = request.headers.get("uid")
    
    if not raw_token or not user_id:
        raise Exception("Invalid Auth information")
    
    token = raw_token.split()[1] # Pega o token que está no header da requisição que está chegando no servidor
    token_information = jwt_handle.decode_jwt_token(token) # Decodifica o token, tira as informações que estão dentro do token
    token_uid = token_information["user_id"]
    
    if user_id and token_uid and (int(token_uid)) == int(user_id):
        return token_information
    
    raise HttpUnauthorizedError("User Unaunthorized")
