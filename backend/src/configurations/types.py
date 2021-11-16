from abc import ABC


class BaseTypeDefinition(ABC):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class Error(BaseTypeDefinition):
    pass


class Success(BaseTypeDefinition):
    pass
