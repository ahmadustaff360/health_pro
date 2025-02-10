## Health Pro

health app for backend

This API provides CRUD operations for managing Health County records in a Frappe-based application.

Endpoints
1. Retrieve All Health Counties
GET http://website-name:8000/api/method/health_pro.health_pro.api.health_county_api.get_health_county

Description:
Returns a list of all health counties.

Response:

{
    "status_code": 200,
    "data": [
        {
            "name": "HC-00005",
            "county_name": "Example County",
            "county_description": "This is an example description."
        },
        {
            "name": "HC-00002",
            "county_name": "Updated County",
            "county_description": "Second Description"
        },
        {
            "name": "HC-00001",
            "county_name": "First County",
            "county_description": "First Description"
        }
    ]
}

2. Create a New Health County

POST http://website-name:8000/api/method/health_pro.health_pro.api.health_county_api.create_health_county

Description:
Creates a new health county with the provided data.

Request Body:
{
  "county_name": "New County",
  "county_description": "Description of the new county"
}

Response:
{
    "status_code": 201,
    "data": {
        "name": "HC-00014",
        "county_name": "Example County",
        "county_description": "This is an example description."
    }
}

3. Update an Existing Health County

PUT http://website-name:8000/api/method/health_pro.health_pro.api.health_county_api.update_health_county?id=HC-00006

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
    "status_code": 200,
    "data": {
        "name": "HC-00012",
        "county_name": "Updated County",
        "county_description": "This is an example description."
    }
}

4. Delete a Health County
DELETE http://website-name:8000/api/method/health_pro.health_pro.api.health_county_api.delete_health_county?id=HC-00006

Description:
Deletes the specified health county.

URL Parameter:
id: The unique ID of the health county to delete.

Response:
{
    "status_code": 200,
    "data": {
        "message": "Health County 'HC-00014' deleted successfully."
    }
}
#### License

mit
