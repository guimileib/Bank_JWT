from .jwt_handler import JWTHandler

def test_jwt_handler():
    jwt_handler = JWTHandler()
    body = {
        "username": "TestandoAqui",
        "aqui": "qualquer coisa",
        "lalala": ""
    }
    
    token = jwt_handler.create_jwt_token(body)
    token_informations = jwt_handler.decode_jwt_token(token)
    
    assert token is not None 
    assert isinstance(token, str)
    assert token_informations["username"] == body["username"]
    assert token_informations["lalala"] == body["lalala"]
    