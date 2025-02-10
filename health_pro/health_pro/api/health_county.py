import json
import frappe
from frappe import _

@frappe.whitelist(methods=["GET"])
def get_health_county():
    
    """Retrieve all health counties."""
    
    try:
        counties = frappe.get_all("Health County", fields=["*"]) 
        return counties
    except Exception as e:
        frappe.throw(_("An unexpected error occurred: {0}").format(str(e)))

@frappe.whitelist(methods=["POST"])
def create_health_county():
    
    """Create a new health county."""
    
    try:
        data = json.loads(frappe.request.data)
        county = frappe.new_doc("Health County")
        
        if not data.get("county_name"):
            frappe.throw(_("County name is required"))
        
        for field, value in data.items():
            if hasattr(county, field):
                setattr(county, field, value)
        county.insert()
        return county.as_dict()
    except Exception as e:
        frappe.throw(_("Failed to create health county: {0}").format(str(e)))

@frappe.whitelist(methods=["PUT"])
def update_health_county(id):
    
    """Update an existing health county."""
    
    try:
        county = frappe.get_doc("Health County", id)
        data = json.loads(frappe.request.data)
        
        for field, value in data.items():
            if hasattr(county, field):
                setattr(county, field, value)
            
        county.save()
        frappe.db.commit()
        
        return county.as_dict()

    except frappe.DoesNotExistError:
        frappe.throw(_("Health County '{0}' not found").format(id))
        
    except Exception as e:
        frappe.throw(_("Failed to update health county: {0}").format(str(e)))

        
@frappe.whitelist(allow_guest=True)
def delete_health_county(id):
    
    """Delete a health county by id."""
    
    try:
        frappe.delete_doc("Health County", id)
        frappe.db.commit()
        return {"message": _("Health County '{0}' deleted successfully").format(id)}
    
    except frappe.DoesNotExistError:
        frappe.throw(_("Health County '{0}' not found").format(id))
        
    except Exception as e:
        frappe.throw(_("Failed to delete health county: {0}").format(str(e)))
