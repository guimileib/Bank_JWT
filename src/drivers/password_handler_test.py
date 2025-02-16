from .password_handler import PasswordHandler

def test_encrypt():
    minha_senha = "123456"
    password_handler = PasswordHandler()
    
    hashed_password = password_handler.encrypt_password(minha_senha)
    #print(hashed_password)
    
    password_check = password_handler.check_password(minha_senha, hashed_password)
    #print(password_check)
    
    assert password_check
    