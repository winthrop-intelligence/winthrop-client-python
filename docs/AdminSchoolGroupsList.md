# AdminSchoolGroupsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminSchoolGroupsListMeta**](AdminSchoolGroupsListMeta.md) |  | [optional] 
**data** | [**List[AdminSchoolGroup]**](AdminSchoolGroup.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_groups_list import AdminSchoolGroupsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolGroupsList from a JSON string
admin_school_groups_list_instance = AdminSchoolGroupsList.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolGroupsList.to_json())

# convert the object into a dict
admin_school_groups_list_dict = admin_school_groups_list_instance.to_dict()
# create an instance of AdminSchoolGroupsList from a dict
admin_school_groups_list_from_dict = AdminSchoolGroupsList.from_dict(admin_school_groups_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


