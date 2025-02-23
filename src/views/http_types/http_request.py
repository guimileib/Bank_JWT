from typing import Dict

class HttpRequest:
    def __init__(
            self, 
            body: Dict = None, 
            headers: Dict = None,
            params: Dict = None,
            token_infos: Dict = None
            ) -> None:
        self.body = body or {}
        self.headers = headers or {}
        self.params = params or {}
        self.token_infos = token_infos or {}
        

        
        