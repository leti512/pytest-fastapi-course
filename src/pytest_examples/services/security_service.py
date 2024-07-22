from fastapi import Request

from dotenv import load_dotenv
from os import getenv

load_dotenv()



from ..dto import SignInSchema

from ..utils.jwt_service import Jwt


from ..exceptions.jwt_exceptions import JwtErrors
class SecurityService:

    def __init__(self):
        self.jwt_service = Jwt()

    async def get_me(self):
        
        response = {}
        response['success'] = True
        response['message'] = 'ok'
        response['payload'] = Request.user
        return response

    async def find_lead_in_service(self, userId):
        return {
            "id": userId,
            "name": "Jhon Doe",
            "password": "123456",
            "address": "street 2",
            "integration": "A"
        }

    async def sign_in(self, input: SignInSchema):

        userid = input['userid']

        find_user = await self.find_lead_in_service(userid)
        
        if not find_user:
            JwtErrors.dont_found_user()

        token = self.jwt_service.encode(find_user)

        response = {}
        response['success'] = True
        response['message'] = 'User found in {}, Token create'.format(find_user['integration'])
        response['payload'] = {}
        response['payload']['token'] = token

        return response