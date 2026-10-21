# MassCopyPositionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copied_count** | **int** |  | 
**copied_ids** | **List[int]** |  | 
**skipped_sports** | **List[str]** | Sports that could not be copied | 
**formatted_next_year** | **str** |  | 

## Example

```python
from winthrop_client_python.models.mass_copy_positions_response import MassCopyPositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MassCopyPositionsResponse from a JSON string
mass_copy_positions_response_instance = MassCopyPositionsResponse.from_json(json)
# print the JSON string representation of the object
print(MassCopyPositionsResponse.to_json())

# convert the object into a dict
mass_copy_positions_response_dict = mass_copy_positions_response_instance.to_dict()
# create an instance of MassCopyPositionsResponse from a dict
mass_copy_positions_response_from_dict = MassCopyPositionsResponse.from_dict(mass_copy_positions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


