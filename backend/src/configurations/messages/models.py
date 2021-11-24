from fastapi import status


class Message:
    message: str
    status_code: status

    def __init__(self, message: str, status_code: status):
        self.message = message
        self.status_code = status_code
