from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        # You can add custom error messages here
        response.data['status_code'] = response.status_code
        response.data['error_message'] = 'Custom error message here.'

    return response