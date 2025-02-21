import jwt
from typing import Dict
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_infos

print()
print("jwt_infos: ", jwt_infos)

class JWTHandler:
    def create_jwt_token(self, body: Dict = {}) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours=int(jwt_infos["JWT_HOURS"])), # Pego o momento de agora e somo um minuto, o token so vai valer durante 1 minuto
                **body # É como se eu tivessando uma parte do dicionario e colocando aqui
            },
            key=jwt_infos["KEY"], # A chave que eu quero usar para encriptar
            algorithm=jwt_infos["ALGORITHM"] # um tipo de encriptação que existe 
        )
        return token
    
    def decode_jwt_token(self, token: str) -> Dict:
        token_information = jwt.decode(
            token, 
            key=jwt_infos["KEY"], 
            algorithms=jwt_infos["ALGORITHM"]
        )
        return token_information
    