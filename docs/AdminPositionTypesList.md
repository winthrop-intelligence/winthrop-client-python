# AdminPositionTypesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminPositionType]**](AdminPositionType.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_position_types_list import AdminPositionTypesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionTypesList from a JSON string
admin_position_types_list_instance = AdminPositionTypesList.from_json(json)
# print the JSON string representation of the object
print(AdminPositionTypesList.to_json())

# convert the object into a dict
admin_position_types_list_dict = admin_position_types_list_instance.to_dict()
# create an instance of AdminPositionTypesList from a dict
admin_position_types_list_from_dict = AdminPositionTypesList.from_dict(admin_position_types_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


