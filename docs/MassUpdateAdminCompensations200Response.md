# MassUpdateAdminCompensations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated** | [**List[AdminCompensation]**](AdminCompensation.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.mass_update_admin_compensations200_response import MassUpdateAdminCompensations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MassUpdateAdminCompensations200Response from a JSON string
mass_update_admin_compensations200_response_instance = MassUpdateAdminCompensations200Response.from_json(json)
# print the JSON string representation of the object
print(MassUpdateAdminCompensations200Response.to_json())

# convert the object into a dict
mass_update_admin_compensations200_response_dict = mass_update_admin_compensations200_response_instance.to_dict()
# create an instance of MassUpdateAdminCompensations200Response from a dict
mass_update_admin_compensations200_response_from_dict = MassUpdateAdminCompensations200Response.from_dict(mass_update_admin_compensations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


