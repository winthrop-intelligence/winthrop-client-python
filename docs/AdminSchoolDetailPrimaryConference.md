# AdminSchoolDetailPrimaryConference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name_display** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_detail_primary_conference import AdminSchoolDetailPrimaryConference

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolDetailPrimaryConference from a JSON string
admin_school_detail_primary_conference_instance = AdminSchoolDetailPrimaryConference.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolDetailPrimaryConference.to_json())

# convert the object into a dict
admin_school_detail_primary_conference_dict = admin_school_detail_primary_conference_instance.to_dict()
# create an instance of AdminSchoolDetailPrimaryConference from a dict
admin_school_detail_primary_conference_from_dict = AdminSchoolDetailPrimaryConference.from_dict(admin_school_detail_primary_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


