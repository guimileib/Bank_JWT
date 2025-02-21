# Fazer a verificação correta do nosso user: vamos colocar uma senha criptografada para um user que está no banco de dados
# Vamos criar um token JWT para esse user
import pytest
from .login_creator import LoginCreator
from src.drivers.password_handler import PasswordHandler

username = "meuUsername"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_password(password) # tem que ser enviado pelo BD

class MockUserRepository:
    def get_user_by_username(self, username: str):
        return (10, username, hashed_password)

def test_create():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(username, password)
    
    print()
    print("response:", response)
    
    assert response["acess"] == True
    assert response["username"] == username
    assert response["token"] is not None
    
def test_create_with_wrong_password():
    login_creator = LoginCreator(MockUserRepository())
    
    with pytest.raises(Exception) as exc:
        login_creator.create(username, "algumaSenhaErrada")
    