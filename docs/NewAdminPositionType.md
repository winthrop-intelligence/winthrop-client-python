# NewAdminPositionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ord** | **int** | The suggested order number, ten past the highest existing one | 
**position_type_groups** | [**List[PositionTypeGroupOption]**](PositionTypeGroupOption.md) | The selectable groups for the form&#39;s \&quot;Grouped?\&quot; select | 

## Example

```python
from winthrop_client_python.models.new_admin_position_type import NewAdminPositionType

# TODO update the JSON string below
json = "{}"
# create an instance of NewAdminPositionType from a JSON string
new_admin_position_type_instance = NewAdminPositionType.from_json(json)
# print the JSON string representation of the object
print(NewAdminPositionType.to_json())

# convert the object into a dict
new_admin_position_type_dict = new_admin_position_type_instance.to_dict()
# create an instance of NewAdminPositionType from a dict
new_admin_position_type_from_dict = NewAdminPositionType.from_dict(new_admin_position_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


