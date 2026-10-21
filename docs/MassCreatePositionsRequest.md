# MassCreatePositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**school_id** | **int** |  | 
**sport_ids** | **List[int]** |  | 
**position_type_ids** | **List[int]** |  | [optional] 
**position_title** | **str** |  | [optional] 
**mass_start_year** | **int** |  | 
**mass_end_year** | **int** |  | 

## Example

```python
from winthrop_client_python.models.mass_create_positions_request import MassCreatePositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassCreatePositionsRequest from a JSON string
mass_create_positions_request_instance = MassCreatePositionsRequest.from_json(json)
# print the JSON string representation of the object
print(MassCreatePositionsRequest.to_json())

# convert the object into a dict
mass_create_positions_request_dict = mass_create_positions_request_instance.to_dict()
# create an instance of MassCreatePositionsRequest from a dict
mass_create_positions_request_from_dict = MassCreatePositionsRequest.from_dict(mass_create_positions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


