# MassCopyPositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**year** | **int** | The season year copied from; positions are copied into the next one | 

## Example

```python
from winthrop_client_python.models.mass_copy_positions_request import MassCopyPositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassCopyPositionsRequest from a JSON string
mass_copy_positions_request_instance = MassCopyPositionsRequest.from_json(json)
# print the JSON string representation of the object
print(MassCopyPositionsRequest.to_json())

# convert the object into a dict
mass_copy_positions_request_dict = mass_copy_positions_request_instance.to_dict()
# create an instance of MassCopyPositionsRequest from a dict
mass_copy_positions_request_from_dict = MassCopyPositionsRequest.from_dict(mass_copy_positions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


