from typing import Optional, Any


class Response:
    def __init__(self, message, status_code: Optional[int] = None) -> None:
        self.message = message
        self.status_code = status_code or 202


class Data:
    def __init__(self, content: Any):
        self.content = content
