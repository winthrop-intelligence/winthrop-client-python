# EditAdminSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | [**AdminSport**](AdminSport.md) |  | 
**time_of_years** | [**List[TimeOfYearOption]**](TimeOfYearOption.md) |  | 

## Example

```python
from winthrop_client_python.models.edit_admin_sport import EditAdminSport

# TODO update the JSON string below
json = "{}"
# create an instance of EditAdminSport from a JSON string
edit_admin_sport_instance = EditAdminSport.from_json(json)
# print the JSON string representation of the object
print(EditAdminSport.to_json())

# convert the object into a dict
edit_admin_sport_dict = edit_admin_sport_instance.to_dict()
# create an instance of EditAdminSport from a dict
edit_admin_sport_from_dict = EditAdminSport.from_dict(edit_admin_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


