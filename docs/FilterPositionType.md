# FilterPositionType

A position type with optional group stub flag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**group_stub** | **bool** |  | [optional] 
**category** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.filter_position_type import FilterPositionType

# TODO update the JSON string below
json = "{}"
# create an instance of FilterPositionType from a JSON string
filter_position_type_instance = FilterPositionType.from_json(json)
# print the JSON string representation of the object
print(FilterPositionType.to_json())

# convert the object into a dict
filter_position_type_dict = filter_position_type_instance.to_dict()
# create an instance of FilterPositionType from a dict
filter_position_type_from_dict = FilterPositionType.from_dict(filter_position_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


