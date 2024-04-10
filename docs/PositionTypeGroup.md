# PositionTypeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**ord** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.position_type_group import PositionTypeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PositionTypeGroup from a JSON string
position_type_group_instance = PositionTypeGroup.from_json(json)
# print the JSON string representation of the object
print(PositionTypeGroup.to_json())

# convert the object into a dict
position_type_group_dict = position_type_group_instance.to_dict()
# create an instance of PositionTypeGroup from a dict
position_type_group_form_dict = position_type_group.from_dict(position_type_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


