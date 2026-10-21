# MassUpdatePositionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated** | [**List[AdminPosition]**](AdminPosition.md) |  | 

## Example

```python
from winthrop_client_python.models.mass_update_positions_response import MassUpdatePositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MassUpdatePositionsResponse from a JSON string
mass_update_positions_response_instance = MassUpdatePositionsResponse.from_json(json)
# print the JSON string representation of the object
print(MassUpdatePositionsResponse.to_json())

# convert the object into a dict
mass_update_positions_response_dict = mass_update_positions_response_instance.to_dict()
# create an instance of MassUpdatePositionsResponse from a dict
mass_update_positions_response_from_dict = MassUpdatePositionsResponse.from_dict(mass_update_positions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


