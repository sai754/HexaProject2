class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed. Incorrect username or password."):
        self.message = message
        super().__init__(self.message)

class ReservationException(Exception):
    def __init__(self, message="Reservation error."):
        self.message = message
        super().__init__(self.message)

class VehicleNotFoundException(Exception):
    def __init__(self, message="Vehicle not found."):
        self.message = message
        super().__init__(self.message)

class AdminNotFoundException(Exception):
    def __init__(self, message="Admin user not found."):
        self.message = message
        super().__init__(self.message)

class InvalidInputException(Exception):
    def __init__(self, message="Invalid input data."):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):
    def __init__(self, message="Database connection error."):
        self.message = message
        super().__init__(self.message)
