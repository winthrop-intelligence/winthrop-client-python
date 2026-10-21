# CreatePositionTypeRequestPositionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**ord** | **int** | Required on create; a whole number of 1 or more, unique across position types | [optional] 
**position_type_group_id** | **int** |  | [optional] 
**group_stub** | **bool** |  | [optional] 
**force_display_title** | **bool** |  | [optional] 
**intercollegiate_only** | **bool** |  | [optional] 
**visible** | **bool** | Whether the position type is published to customer catalogs | [optional] 

## Example

```python
from winthrop_client_python.models.create_position_type_request_position_type import CreatePositionTypeRequestPositionType

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePositionTypeRequestPositionType from a JSON string
create_position_type_request_position_type_instance = CreatePositionTypeRequestPositionType.from_json(json)
# print the JSON string representation of the object
print(CreatePositionTypeRequestPositionType.to_json())

# convert the object into a dict
create_position_type_request_position_type_dict = create_position_type_request_position_type_instance.to_dict()
# create an instance of CreatePositionTypeRequestPositionType from a dict
create_position_type_request_position_type_from_dict = CreatePositionTypeRequestPositionType.from_dict(create_position_type_request_position_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


