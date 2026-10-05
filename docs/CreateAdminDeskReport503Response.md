# CreateAdminDeskReport503Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | 
**draft_uuid** | **UUID** |  | 

## Example

```python
from winthrop_client_python.models.create_admin_desk_report503_response import CreateAdminDeskReport503Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminDeskReport503Response from a JSON string
create_admin_desk_report503_response_instance = CreateAdminDeskReport503Response.from_json(json)
# print the JSON string representation of the object
print(CreateAdminDeskReport503Response.to_json())

# convert the object into a dict
create_admin_desk_report503_response_dict = create_admin_desk_report503_response_instance.to_dict()
# create an instance of CreateAdminDeskReport503Response from a dict
create_admin_desk_report503_response_from_dict = CreateAdminDeskReport503Response.from_dict(create_admin_desk_report503_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


