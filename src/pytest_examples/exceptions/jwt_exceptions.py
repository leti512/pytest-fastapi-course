from . import Error

class JwtErrors:
    """
    JwtErrors is a class that encapsulates various JWT-related errors as class methods.
    Each method raises an Error with a specific HTTP status code and error message.
    """
    @staticmethod
    def token_not_found():
        """Raises an error indicating that no valid JWT token was found in the request."""
        Error(401, "no valid token was found in the request")

    @staticmethod
    def invalid_token():
        """Raises an error indicating that the provided JWT token is invalid."""
        Error(401, "your token is invalid, please log in again")

    @staticmethod
    def bearer_not_found():
        """Raises an error indicating that the 'Bearer' keyword is missing before the token."""
        Error(400, "it is necessary to send the word bearer before the token")

    @staticmethod
    def environment_variables_not_found():
        """Raises an error indicating that necessary environment variables are not set."""
        Error(500, "no environment variables were set, contact your administrator")

    @staticmethod
    def missing_params():
        """Raises an error indicating that there are missing parameters in the request body."""
        Error(400, "missing parameters in request body")

    @staticmethod
    def dont_found_user():
        """Raises an error indicating that the user credentials are incorrect."""
        Error(401, "Tpid or page_id incorrect")

    @staticmethod
    def dont_permission_access(ip: str):
        """Raises an error indicating that the IP address is not whitelisted."""
        Error(403, "the ip %s is not whitelisted" % (ip))

    @staticmethod
    def not_exist_configuration():
        """Raises an error indicating that the configuration does not exist."""
        Error(404, "the configuration is enable")