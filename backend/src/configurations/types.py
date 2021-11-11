from configurations.errors.generic import GenericErrors


class Error:
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __init__(self):
        self.code = GenericErrors.SERVER_ERROR.name
        self.message = GenericErrors.SERVER_ERROR.value
