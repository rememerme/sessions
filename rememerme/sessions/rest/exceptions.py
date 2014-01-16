from rest_framework.exceptions import APIException

class BadRequestException(APIException):
    '''
        Bad Request Exception.
    '''
    status_code = 400
    detail = "A Bad Request was made for the API. Revise input parameters."

class SessionAuthorizationException(APIException):
    '''
        The user was not correctly authorized.
    '''
    status_code = 401
    detail = "Incorrect password, username combination."
    
class SessionNotFoundException(APIException):
    '''
        The requested user was not found.
    '''
    status_code = 400
    detail = "The session requested does not exist."

class NotImplementedException(APIException):
    '''
        The API method was not implemented yet.
    '''
    status_code = 400
    detail = "This API method has not been implemented."