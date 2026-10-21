# AdminSchoolNamesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminCoachContractsQcListMeta**](AdminCoachContractsQcListMeta.md) |  | [optional] 
**data** | [**List[AdminSchoolName]**](AdminSchoolName.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_names_list import AdminSchoolNamesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolNamesList from a JSON string
admin_school_names_list_instance = AdminSchoolNamesList.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolNamesList.to_json())

# convert the object into a dict
admin_school_names_list_dict = admin_school_names_list_instance.to_dict()
# create an instance of AdminSchoolNamesList from a dict
admin_school_names_list_from_dict = AdminSchoolNamesList.from_dict(admin_school_names_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


