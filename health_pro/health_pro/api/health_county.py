
import json
import frappe
from frappe import _
from .response_utils import (
    success_response,
    error_response,
    not_found_response,
    missing_field_response,
    creation_failed_response,
    update_failed_response,
    deletion_failed_response,
    created_successfully_response
)

class HealthCountyAPI:
    """API for Health County CRUD operations with minimal response data."""

    def get(self):
        """Retrieve all health counties with selected fields only."""
        try:
            counties = frappe.get_all(
                "Health County",
                fields=["name", "county_name", "county_description"]
            )
            return success_response(counties)
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Get Error")
            return error_response()

    def create(self):
        """Create a new health county and return minimal data."""
        try:
            data = json.loads(frappe.request.data)
            if not data.get("county_name"):
                return missing_field_response("county_name")
            
            county = frappe.new_doc("Health County")
            county.update({
                "county_name": data.get("county_name"),
                "county_description": data.get("county_description")
            })
            county.insert()
            frappe.db.commit()

            return created_successfully_response({
                "name": county.name,
                "county_name": county.county_name,
                "county_description": county.county_description
            })
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Create Error")
            return creation_failed_response()

    def update(self, id):
        """Update an existing health county and return updated data."""
        try:
            county = frappe.get_doc("Health County", id)
            data = json.loads(frappe.request.data)
            
            if "county_name" in data:
                county.county_name = data["county_name"]
            if "county_description" in data:
                county.county_description = data["county_description"]

            county.save()
            frappe.db.commit()

            return success_response({
                "name": county.name,
                "county_name": county.county_name,
                "county_description": county.county_description
            })
        except frappe.DoesNotExistError:
            return not_found_response("Health County", id)
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Update Error")
            return update_failed_response()

    def delete(self, id):
        """Delete a health county by ID."""
        try:
            county = frappe.get_doc("Health County", id)
            county.delete()
            frappe.db.commit()
            return success_response({"message": f"Health County '{id}' deleted successfully."})
        except frappe.DoesNotExistError:
            return not_found_response("Health County", id)
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Delete Error")
            return deletion_failed_response()
