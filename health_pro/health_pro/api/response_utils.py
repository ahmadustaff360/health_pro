# """General Respone Functions"""


def success_response(data, status_code=200):
    """General success response without 'message' key and with content_type."""
    return data, status_code

def error_response(status_code=400):
    """General error response."""
    return status_code

def not_found_response(resource_name, resource_id, status_code=404):
    """Resource not found response."""
    return f"{resource_name} '{resource_id}' not found.", status_code

def missing_field_response(field_name):
    """Response for missing required field."""
    return f"{field_name} is required.", 400

def created_successfully_response(data):
    """Response for successful creation."""
    return data, 201

def creation_failed_response():
    """Response for failed creation."""
    return "Failed to create the resource.", 500

def update_failed_response():
    """Response for failed update."""
    return "Failed to update the resource.", 500

def deletion_failed_response():
    """Response for failed deletion."""
    return "Failed to delete the resource.", 500
