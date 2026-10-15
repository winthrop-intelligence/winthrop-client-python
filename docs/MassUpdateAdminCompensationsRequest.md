# MassUpdateAdminCompensationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**compensations** | [**List[MassUpdateAdminCompensationsRequestCompensationsInner]**](MassUpdateAdminCompensationsRequestCompensationsInner.md) |  | 

## Example

```python
from winthrop_client_python.models.mass_update_admin_compensations_request import MassUpdateAdminCompensationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassUpdateAdminCompensationsRequest from a JSON string
mass_update_admin_compensations_request_instance = MassUpdateAdminCompensationsRequest.from_json(json)
# print the JSON string representation of the object
print(MassUpdateAdminCompensationsRequest.to_json())

# convert the object into a dict
mass_update_admin_compensations_request_dict = mass_update_admin_compensations_request_instance.to_dict()
# create an instance of MassUpdateAdminCompensationsRequest from a dict
mass_update_admin_compensations_request_from_dict = MassUpdateAdminCompensationsRequest.from_dict(mass_update_admin_compensations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


