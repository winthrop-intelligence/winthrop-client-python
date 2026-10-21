# MassDepartPositionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departed_ids** | **List[int]** |  | 
**failed** | [**List[MassDepartPositionFailure]**](MassDepartPositionFailure.md) | Positions that could not be departed; the others are departed regardless | 

## Example

```python
from winthrop_client_python.models.mass_depart_positions_response import MassDepartPositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MassDepartPositionsResponse from a JSON string
mass_depart_positions_response_instance = MassDepartPositionsResponse.from_json(json)
# print the JSON string representation of the object
print(MassDepartPositionsResponse.to_json())

# convert the object into a dict
mass_depart_positions_response_dict = mass_depart_positions_response_instance.to_dict()
# create an instance of MassDepartPositionsResponse from a dict
mass_depart_positions_response_from_dict = MassDepartPositionsResponse.from_dict(mass_depart_positions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


