"""General Respone Functions"""

def success_response(message, data=None, status_code=200):
    """General success response."""
    return {
        "status": "success",
        "message": message,
        "data": data
    }, status_code


def error_response(message, data=None, status_code=400):
    """General error response."""
    return {
        "status": "error",
        "message": message,
        "data": data
    }, status_code


def not_found_response(resource_name, resource_id):
    """Response when a resource is not found."""
    return {
        "status": "error",
        "message": f"{resource_name} '{resource_id}' not found.",
        "data": None
    }, 404


def missing_field_response(field_name):
    """Response for missing required field."""
    return {
        "status": "error",
        "message": f"{field_name} is required.",
        "data": None
    }, 400


def unexpected_error_response():
    """Response for unexpected server errors."""
    return {
        "status": "error",
        "message": "An unexpected error occurred.",
        "data": None
    }, 500


def created_successfully_response(resource_name, data):
    """Response for successful resource creation."""
    return {
        "status": "success",
        "message": f"{resource_name} created successfully.",
        "data": data
    }, 201


def creation_failed_response(resource_name):
    """Response when creation fails."""
    return {
        "status": "error",
        "message": f"Failed to create {resource_name}.",
        "data": None
    }, 500


def update_failed_response(resource_name):
    """Response when update fails."""
    return {
        "status": "error",
        "message": f"Failed to update {resource_name}.",
        "data": None
    }, 500


def deletion_failed_response(resource_name):
    """Response when deletion fails."""
    return {
        "status": "error",
        "message": f"Failed to delete {resource_name}.",
        "data": None
    }, 500
