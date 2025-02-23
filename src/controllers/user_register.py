from typing import Dict
from src.models.interface.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from src.controllers.interfaces.user_register import UserRegisterInterface

class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None: 
        self.__user_repository = user_repository
        self.__password_handle = PasswordHandler()
    
    # Método público para registrar um novo usuário
    def registry(self, username: str, password: str) -> Dict:
        hashed_password = self.__create_hash_password(password)
        self.__registry_new_user(username, hashed_password)
        return self.__format_response(username)
        
    # Cria a senha criptografada
    def __create_hash_password(self, password: str) -> str:
        hash_password = self.__password_handle.encrypt_password(password)
        return hash_password
    
    # Faço o registro do usuário
    def __registry_new_user(self, username: str, hashed_password: str) -> None:
        self.__user_repository.registry_user(username, hashed_password)
    
    # Lugar a o retorno da informação 
    def __format_response(self, username: str) -> Dict:
        return {
            "type": "User",
            "count": 1,
            "username": username
        }