# PositionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**ord** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**position_type_group** | [**PositionTypeGroup**](PositionTypeGroup.md) |  | [optional] 
**force_display_title** | **bool** |  | [optional] 
**intercollegiate_only** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.position_type import PositionType

# TODO update the JSON string below
json = "{}"
# create an instance of PositionType from a JSON string
position_type_instance = PositionType.from_json(json)
# print the JSON string representation of the object
print(PositionType.to_json())

# convert the object into a dict
position_type_dict = position_type_instance.to_dict()
# create an instance of PositionType from a dict
position_type_from_dict = PositionType.from_dict(position_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


