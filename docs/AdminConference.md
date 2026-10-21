# AdminConference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**headquarters** | **str** |  | [optional] 
**founded** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**external_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**division** | [**AdminSchoolDetailPrimaryConference**](AdminSchoolDetailPrimaryConference.md) |  | [optional] 
**schools_count** | **int** |  | [optional] 
**full_member_schools_count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_conference import AdminConference

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConference from a JSON string
admin_conference_instance = AdminConference.from_json(json)
# print the JSON string representation of the object
print(AdminConference.to_json())

# convert the object into a dict
admin_conference_dict = admin_conference_instance.to_dict()
# create an instance of AdminConference from a dict
admin_conference_from_dict = AdminConference.from_dict(admin_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


