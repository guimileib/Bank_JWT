from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
from unittest.mock import Mock

# Interação mockada do __conn e do cursor

# Mapeando quais são os comandos SQL que estamos jogando para dentro do cursor
class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()
        
class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_registry_user():
    username = "fred"
    password = "Yabadabadoo"
    
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    
    repo.registry_user(username, password)   
    
    cursor = mock_connection.cursor.return_value
    
    # Verifica se possui um dos comandos SQL que estamos jogando para dentro do cursor
    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)
    
def test_edit_balance():
    user_id = 244
    balance = 190.09
    
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    
    repo.edit_balance(user_id, balance)   
    
    cursor = mock_connection.cursor.return_value

    # Testa o que está enviando em tupla no cursor.execute
    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (balance, user_id)
    
    mock_connection.commit.assert_called_once() # Verifica se o commit foi chamado pelo menos uma vez
    
def test_get_user_by_username():
    username = "meuUsername"
    
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    
    repo.get_user_by_username(username)   
    
    cursor = mock_connection.cursor.return_value

    # Testa o que está enviando em tupla no cursor.execute
    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)
    
    cursor.fetchone.assert_called_once()  # Verifica se o fetchone foi chamado pelo menos uma vez
    