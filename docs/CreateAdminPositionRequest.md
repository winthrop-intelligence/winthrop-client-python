# CreateAdminPositionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**CreateAdminPositionRequestPosition**](CreateAdminPositionRequestPosition.md) |  | 
**position_departure** | [**CreateAdminPositionRequestPositionDeparture**](CreateAdminPositionRequestPositionDeparture.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_position_request import CreateAdminPositionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminPositionRequest from a JSON string
create_admin_position_request_instance = CreateAdminPositionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminPositionRequest.to_json())

# convert the object into a dict
create_admin_position_request_dict = create_admin_position_request_instance.to_dict()
# create an instance of CreateAdminPositionRequest from a dict
create_admin_position_request_from_dict = CreateAdminPositionRequest.from_dict(create_admin_position_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


