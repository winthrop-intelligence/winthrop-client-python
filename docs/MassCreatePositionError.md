# MassCreatePositionError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_id** | **int** |  | 
**errors** | **List[str]** |  | 

## Example

```python
from winthrop_client_python.models.mass_create_position_error import MassCreatePositionError

# TODO update the JSON string below
json = "{}"
# create an instance of MassCreatePositionError from a JSON string
mass_create_position_error_instance = MassCreatePositionError.from_json(json)
# print the JSON string representation of the object
print(MassCreatePositionError.to_json())

# convert the object into a dict
mass_create_position_error_dict = mass_create_position_error_instance.to_dict()
# create an instance of MassCreatePositionError from a dict
mass_create_position_error_from_dict = MassCreatePositionError.from_dict(mass_create_position_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


