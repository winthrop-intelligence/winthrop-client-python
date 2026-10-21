# MassUpdatePositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**positions** | [**List[MassUpdatePositionRow]**](MassUpdatePositionRow.md) | All rows are saved or none (one failing row rolls back the batch) | 

## Example

```python
from winthrop_client_python.models.mass_update_positions_request import MassUpdatePositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassUpdatePositionsRequest from a JSON string
mass_update_positions_request_instance = MassUpdatePositionsRequest.from_json(json)
# print the JSON string representation of the object
print(MassUpdatePositionsRequest.to_json())

# convert the object into a dict
mass_update_positions_request_dict = mass_update_positions_request_instance.to_dict()
# create an instance of MassUpdatePositionsRequest from a dict
mass_update_positions_request_from_dict = MassUpdatePositionsRequest.from_dict(mass_update_positions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


