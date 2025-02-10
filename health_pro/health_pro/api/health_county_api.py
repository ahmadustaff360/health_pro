import frappe
from .health_county import HealthCountyAPI 

api = HealthCountyAPI()

@frappe.whitelist(methods=["GET"])
def get_health_county():
    response, status_code = api.get()
    frappe.local.response.status_code = status_code
    return response

@frappe.whitelist(methods=["POST"])
def create_health_county():
    response, status_code = api.create()
    frappe.local.response.status_code = status_code
    return response

@frappe.whitelist(methods=["PUT"])
def update_health_county(id):
    response, status_code = api.update(id)
    frappe.local.response.status_code = status_code
    return response

@frappe.whitelist(methods=["DELETE"])
def delete_health_county(id):
    response, status_code = api.delete(id)
    frappe.local.response.status_code = status_code
    return response
