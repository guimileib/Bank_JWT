from .user_register import UserRegister

# Mock imita o Repositorio do usuário
class MockUserRepository:
    def __init__(self) -> None:
        self.registry_user_attributtes = {}

    def registry_user(self, username, password) -> None:
        self.registry_user_attributtes["username"] = username
        self.registry_user_attributtes["password"] = password

def test_registry():
    repository = MockUserRepository()
    controller = UserRegister(repository)
    
    username = "olaMundo"
    password = "myPassword"
    
    response = controller.registry(username, password)

    assert response["type"] == "User"
    assert response["username"] == username
    
    assert repository.registry_user_attributtes["username"] == username
    assert repository.registry_user_attributtes["password"] is not None
    assert repository.registry_user_attributtes["password"] != password