# PositionEntry

Per-school position record backing an aggregate stat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.position_entry import PositionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PositionEntry from a JSON string
position_entry_instance = PositionEntry.from_json(json)
# print the JSON string representation of the object
print(PositionEntry.to_json())

# convert the object into a dict
position_entry_dict = position_entry_instance.to_dict()
# create an instance of PositionEntry from a dict
position_entry_from_dict = PositionEntry.from_dict(position_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


