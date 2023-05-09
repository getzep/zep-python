
    Attributes
    ----------
    code : int
        The error code associated with the API error.
    message : str
        The error message associated with the API error.
    """
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message