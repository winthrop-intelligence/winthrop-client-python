# AdminConferenceSchoolDirectoryRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**school_status** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**allows_foia** | **bool** |  | [optional] 
**cost_of_living_index_city_code** | **str** |  | [optional] 
**primary_conference_name** | **str** |  | [optional] 
**division_name** | **str** |  | [optional] 
**subdivisions** | [**List[AdminCompensationListMetaContractStatusOptionsInner]**](AdminCompensationListMetaContractStatusOptionsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_conference_school_directory_row import AdminConferenceSchoolDirectoryRow

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConferenceSchoolDirectoryRow from a JSON string
admin_conference_school_directory_row_instance = AdminConferenceSchoolDirectoryRow.from_json(json)
# print the JSON string representation of the object
print(AdminConferenceSchoolDirectoryRow.to_json())

# convert the object into a dict
admin_conference_school_directory_row_dict = admin_conference_school_directory_row_instance.to_dict()
# create an instance of AdminConferenceSchoolDirectoryRow from a dict
admin_conference_school_directory_row_from_dict = AdminConferenceSchoolDirectoryRow.from_dict(admin_conference_school_directory_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


