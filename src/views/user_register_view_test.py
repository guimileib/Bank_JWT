import pytest
from src.views.user_register_view import UserRegisterView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class MockController:
    def registry(self, username, password):
        return {"aluma": "coisa"}

def test_handle_user_register():
    body = {
        "username": "test",
        "password": "test"
    }
    request = HttpRequest(body=body)
    
    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)
    
    with pytest.raises(Exception):
        user_register_view.handle(request)

