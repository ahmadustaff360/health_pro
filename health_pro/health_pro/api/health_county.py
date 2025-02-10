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
            fields = frappe.get_meta("Health County").fields
            field_names = [field.fieldname for field in fields if field.fieldtype != "Table"]
            
            if 'name' not in field_names:
                field_names.append('name')

            counties = frappe.get_all(
                "Health County",
                fields=field_names
            )
            return success_response(counties)
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Get Error")
            return error_response()

    def create(self):
        """Create a new health county and return minimal data."""
        try:
            data = json.loads(frappe.request.data)
            
            fields = [
                field.fieldname 
                for field in frappe.get_meta("Health County").fields 
                if field.fieldtype != "Table"
            ]
            
            mandatory_fields = [
                field.fieldname 
                for field in frappe.get_meta("Health County").fields 
                if field.reqd
            ]
            
            for field in mandatory_fields:
                if field not in data:
                    return missing_field_response(field)
            
            county = frappe.new_doc("Health County")
            for field, value in data.items():
                if field in fields:
                    county.set(field, value)
            
            county.insert()
            frappe.db.commit()

            county_data = {field: getattr(county, field) for field in fields}
            county_data['name'] = county.name

            return created_successfully_response(county_data)
        except Exception as e:
            frappe.log_error(message=str(e), title="Health County Create Error")
            return creation_failed_response()

    def update(self, id):
        """Update an existing health county and return updated data."""
        try:
            county = frappe.get_doc("Health County", id)
            data = json.loads(frappe.request.data)
            fields = [field.fieldname for field in frappe.get_meta("Health County").fields if field.fieldtype != "Table"]

            for field, value in data.items():
                if field in fields:
                    county.set(field, value)

            county.save()
            frappe.db.commit()
            updated_data = {field: getattr(county, field) for field in fields}
            updated_data['name'] = county.name

            return success_response(updated_data)

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
