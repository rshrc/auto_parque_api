from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Invalid RFID Code'
    default_code = 'Invalid'