# AdminPositionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminPosition]**](AdminPosition.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_positions_list import AdminPositionsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionsList from a JSON string
admin_positions_list_instance = AdminPositionsList.from_json(json)
# print the JSON string representation of the object
print(AdminPositionsList.to_json())

# convert the object into a dict
admin_positions_list_dict = admin_positions_list_instance.to_dict()
# create an instance of AdminPositionsList from a dict
admin_positions_list_from_dict = AdminPositionsList.from_dict(admin_positions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


