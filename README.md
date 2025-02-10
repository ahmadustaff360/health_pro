## Health Pro

health app for backend

This API provides CRUD operations for managing Health County records in a Frappe-based application.

Endpoints
1. Retrieve All Health Counties
GET http://website-name:8000/api/method/health_pro.health_pro.api.health_county.get_health_county

Description:
Returns a list of all health counties.

Response:

{
    "message": [
        {
            "name": "HC-00002",
            "creation": "2025-02-09 23:25:18.840048",
            "modified": "2025-02-10 01:15:55.237489",
            "modified_by": "Administrator",
            "owner": "Administrator",
            "docstatus": 0,
            "idx": 0,
            "_user_tags": null,
            "_comments": null,
            "_assign": null,
            "_liked_by": null,
            "county_name": "Second County",
            "county_description": "Second Description"
        }
        
    ]
}

2. Create a New Health County

POST http://website-name:8000/api/method/health_pro.health_pro.api.health_county.create_health_county

Description:
Creates a new health county with the provided data.

Request Body:
{
  "county_name": "New County",
  "county_description": "Description of the new county"
}

Response:
{
    "message": {
        "name": "HC-00006",
        "owner": "Administrator",
        "creation": "2025-02-10 11:26:52.204645",
        "modified": "2025-02-10 11:26:52.204645",
        "modified_by": "Administrator",
        "docstatus": 0,
        "idx": 0,
        "county_name": "New County",
        "county_description": "Description of the new county.",
        "doctype": "Health County"
    }
}

3. Update an Existing Health County

PUT http://website-name:8000/api/method/health_pro.health_pro.api.health_county.update_health_county?id=HC-00006

Description:
Updates the specified health county with the provided data.

URL Parameter:
id: The unique ID of the health county to update.

Request Body:
{
  "county_name": "Updated County Name",
  "county_description": "Updated description"
}

Response:
{
    "message": {
        "name": "HC-00006",
        "owner": "Administrator",
        "creation": "2025-02-10 11:26:52.204645",
        "modified": "2025-02-10 11:28:51.177934",
        "modified_by": "Administrator",
        "docstatus": 0,
        "idx": 0,
        "county_name": "Updated County Name",
        "county_description": "Udpated Description.",
        "doctype": "Health County"
    }
}

4. Delete a Health County
DELETE http://website-name:8000/api/method/health_pro.health_pro.api.health_county.delete_health_county?id=HC-00006

Description:
Deletes the specified health county.

URL Parameter:
id: The unique ID of the health county to delete.

Response:
{
  "message": "Health County 'County ID' deleted successfully"
}

Error Handling
All endpoints return a standardized error message if an exception occurs. Example:
{
    "message": {
        "message": "Health County 'HC-00006' deleted successfully"
    }
}
#### License

mit
