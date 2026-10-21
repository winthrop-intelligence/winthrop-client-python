# AdminSportsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**data** | [**List[AdminSport]**](AdminSport.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_sports_list import AdminSportsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSportsList from a JSON string
admin_sports_list_instance = AdminSportsList.from_json(json)
# print the JSON string representation of the object
print(AdminSportsList.to_json())

# convert the object into a dict
admin_sports_list_dict = admin_sports_list_instance.to_dict()
# create an instance of AdminSportsList from a dict
admin_sports_list_from_dict = AdminSportsList.from_dict(admin_sports_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


