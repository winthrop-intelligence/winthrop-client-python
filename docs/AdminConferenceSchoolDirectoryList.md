# AdminConferenceSchoolDirectoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminConferenceSchoolDirectoryRow]**](AdminConferenceSchoolDirectoryRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_conference_school_directory_list import AdminConferenceSchoolDirectoryList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConferenceSchoolDirectoryList from a JSON string
admin_conference_school_directory_list_instance = AdminConferenceSchoolDirectoryList.from_json(json)
# print the JSON string representation of the object
print(AdminConferenceSchoolDirectoryList.to_json())

# convert the object into a dict
admin_conference_school_directory_list_dict = admin_conference_school_directory_list_instance.to_dict()
# create an instance of AdminConferenceSchoolDirectoryList from a dict
admin_conference_school_directory_list_from_dict = AdminConferenceSchoolDirectoryList.from_dict(admin_conference_school_directory_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


