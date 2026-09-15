# ValidateAdminDeskReport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[DeskFinding]**](DeskFinding.md) |  | 
**publish_blocked** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.validate_admin_desk_report200_response import ValidateAdminDeskReport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAdminDeskReport200Response from a JSON string
validate_admin_desk_report200_response_instance = ValidateAdminDeskReport200Response.from_json(json)
# print the JSON string representation of the object
print(ValidateAdminDeskReport200Response.to_json())

# convert the object into a dict
validate_admin_desk_report200_response_dict = validate_admin_desk_report200_response_instance.to_dict()
# create an instance of ValidateAdminDeskReport200Response from a dict
validate_admin_desk_report200_response_from_dict = ValidateAdminDeskReport200Response.from_dict(validate_admin_desk_report200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


