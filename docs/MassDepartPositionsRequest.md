# MassDepartPositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**year** | **int** |  | 

## Example

```python
from winthrop_client_python.models.mass_depart_positions_request import MassDepartPositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassDepartPositionsRequest from a JSON string
mass_depart_positions_request_instance = MassDepartPositionsRequest.from_json(json)
# print the JSON string representation of the object
print(MassDepartPositionsRequest.to_json())

# convert the object into a dict
mass_depart_positions_request_dict = mass_depart_positions_request_instance.to_dict()
# create an instance of MassDepartPositionsRequest from a dict
mass_depart_positions_request_from_dict = MassDepartPositionsRequest.from_dict(mass_depart_positions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


