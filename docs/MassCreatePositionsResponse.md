# MassCreatePositionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**List[AdminPosition]**](AdminPosition.md) |  | 
**errors** | [**List[MassCreatePositionError]**](MassCreatePositionError.md) | One entry per season whose position could not be created | 

## Example

```python
from winthrop_client_python.models.mass_create_positions_response import MassCreatePositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MassCreatePositionsResponse from a JSON string
mass_create_positions_response_instance = MassCreatePositionsResponse.from_json(json)
# print the JSON string representation of the object
print(MassCreatePositionsResponse.to_json())

# convert the object into a dict
mass_create_positions_response_dict = mass_create_positions_response_instance.to_dict()
# create an instance of MassCreatePositionsResponse from a dict
mass_create_positions_response_from_dict = MassCreatePositionsResponse.from_dict(mass_create_positions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


