import jwt
from typing import Dict
from datetime import datetime, timedelta, timezone

class JWTHandler:
    def create_jwt_token(self, body: Dict = {}) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(minutes=1), # Pego o momento de agora e somo um minuto, o token so vai valer durante 1 minuto
                **body # É como se eu tivessando uma parte do dicionario e colocando aqui
            },
            key="minhaChave",
            algorithm='HS256' # um tipo de encriptação que existe 
        )
        return token
    
    def decode_jwt_token(self, token: str) -> Dict:
        token_information = jwt.decode(
            token, 
            key="minhaChave", 
            algorithms=['HS256']
        )
        return token_information
    