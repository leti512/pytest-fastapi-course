from jwt import encode, decode, exceptions
from os import getenv
from ..exceptions.jwt_exceptions import JwtErrors
import logging

class Jwt:
    """
    Jwt is a class responsible for handling JSON Web Tokens (JWT) operations such as encoding and decoding.
    It uses environment variables to retrieve the secret key and algorithm used for the JWT operations.
    """

    def __init__(self):
        """
        Initializes the Jwt instance by retrieving the SECRET_KEY and ALGORITHM from environment variables.
        """
        self.secret = getenv("SECRET_KEY")
        self.algorith = getenv("ALGORITHM")

    def encode(self, user):
        """
        Encodes the user information into a JWT.

        Args:
            user (dict): A dictionary containing the user information to be encoded.

        Returns:
            str: The encoded JWT as a string.

        Raises:
            JwtErrors: If the environment variables are not set or if the token encoding fails.
        """
        try:
            if not self.secret or not self.algorith:
                JwtErrors.environment_variables_not_found()
            return encode(user, self.secret, algorithm=self.algorith)
        except exceptions.InvalidTokenError as error:
            logging.warning(str(error))

    def decode(self, token: str):
        """
        Decodes the JWT back into user information.

        Args:
            token (str): The JWT string to be decoded.

        Returns:
            dict: The decoded user information.

        Raises:
            JwtErrors: If the environment variables are not set or if the token decoding fails.
        """
        try:
            if not self.secret or not self.algorith:
                JwtErrors.environment_variables_not_found()
            return decode(token, self.secret, algorithms=[self.algorith])
        except exceptions.DecodeError as error:
            logging.warning(str(error))