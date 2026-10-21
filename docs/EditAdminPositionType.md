# EditAdminPositionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_type** | [**AdminPositionType**](AdminPositionType.md) |  | 
**position_type_groups** | [**List[PositionTypeGroupOption]**](PositionTypeGroupOption.md) | The selectable groups for the form&#39;s \&quot;Grouped?\&quot; select | 

## Example

```python
from winthrop_client_python.models.edit_admin_position_type import EditAdminPositionType

# TODO update the JSON string below
json = "{}"
# create an instance of EditAdminPositionType from a JSON string
edit_admin_position_type_instance = EditAdminPositionType.from_json(json)
# print the JSON string representation of the object
print(EditAdminPositionType.to_json())

# convert the object into a dict
edit_admin_position_type_dict = edit_admin_position_type_instance.to_dict()
# create an instance of EditAdminPositionType from a dict
edit_admin_position_type_from_dict = EditAdminPositionType.from_dict(edit_admin_position_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


