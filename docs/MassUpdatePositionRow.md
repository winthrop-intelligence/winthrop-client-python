# MassUpdatePositionRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**position_type_ids** | **List[int]** |  | [optional] 
**creation_reason** | **str** |  | [optional] 
**article_link** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.mass_update_position_row import MassUpdatePositionRow

# TODO update the JSON string below
json = "{}"
# create an instance of MassUpdatePositionRow from a JSON string
mass_update_position_row_instance = MassUpdatePositionRow.from_json(json)
# print the JSON string representation of the object
print(MassUpdatePositionRow.to_json())

# convert the object into a dict
mass_update_position_row_dict = mass_update_position_row_instance.to_dict()
# create an instance of MassUpdatePositionRow from a dict
mass_update_position_row_from_dict = MassUpdatePositionRow.from_dict(mass_update_position_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


