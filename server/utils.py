from django.http import JsonResponse

def success_response(message="Success", data=None, status_code=200):
    response = {
        "success": True,
        "message": message,
    }
    if data is not None:
        response["data"] = data
    return JsonResponse(response, status=status_code)


def error_response(error="Something went wrong", details=None, status_code=400):
    response = {
        "success": False,
        "error": error,
    }
    if details is not None:
        response["details"] = details
    return JsonResponse(response, status=status_code)
