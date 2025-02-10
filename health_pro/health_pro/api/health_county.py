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
    unexpected_error_response,
    created_successfully_response
)

class HealthCountyAPI:
    """API for Health County CRUD operations."""

    def get(self):
        """Retrieve all health counties."""
        try:
            counties = frappe.get_all("Health County", fields=["*"])
            return success_response("Fetched all health counties successfully.", counties)
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Get Error")
            return unexpected_error_response()

    def create(self):
        """Create a new health county."""
        try:
            data = json.loads(frappe.request.data)
            if not data.get("county_name"):
                return missing_field_response("County name")

            county = frappe.new_doc("Health County")
            for field, value in data.items():
                if hasattr(county, field):
                    setattr(county, field, value)
                    
            county.insert()
            frappe.db.commit()
            return created_successfully_response("Health County", county.as_dict())
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Create Error")
            return creation_failed_response("health county")

    def update(self, id):
        """Update an existing health county."""
        try:
            county = frappe.get_doc("Health County", id)
            data = json.loads(frappe.request.data)
            for field, value in data.items():
                if hasattr(county, field):
                    setattr(county, field, value)
                    
            county.save()
            frappe.db.commit()
            return success_response("Health county updated successfully.", county.as_dict())
        except frappe.DoesNotExistError:
            return not_found_response("Health County", id)
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Update Error")
            return update_failed_response("health county")

    def delete(self, id):
        """Delete a health county by id."""
        try:
            county = frappe.get_doc("Health County", id)
            county.delete()
            frappe.db.commit()
            return success_response(f"Health County '{id}' deleted successfully.")
        except frappe.DoesNotExistError:
            return not_found_response("Health County", id)
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Delete Error")
            return deletion_failed_response("health county")
