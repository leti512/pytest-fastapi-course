from os import getenv
from dotenv import load_dotenv
load_dotenv()

from ..dto import MainOutputSchema

class MainService:
    """
    MainService is a service class responsible for handling the main operations of the application.
    It provides a method to start the service and return a response indicating the server status,
    including the version retrieved from environment variables.
    """

    @staticmethod
    def start() -> MainOutputSchema:
        """
        Starts the main service and returns a structured response containing the server status.

        Returns:
            MainOutputSchema: A dictionary containing the success status, a message, and the server version.
        """
        response: MainOutputSchema = {}
        response["success"] = True
        response["message"] = "Server running correctly"
        response["version"] = str(getenv("VERSION"))
        return response