# AdminConferenceDetail


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
**subdivision_options** | [**List[AdminCompensationListMetaContractStatusOptionsInner]**](AdminCompensationListMetaContractStatusOptionsInner.md) |  | [optional] 
**direct_subdivisions** | [**List[AdminCompensationListMetaContractStatusOptionsInner]**](AdminCompensationListMetaContractStatusOptionsInner.md) |  | [optional] 
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**full_member_schools** | [**List[IdName]**](IdName.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_conference_detail import AdminConferenceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConferenceDetail from a JSON string
admin_conference_detail_instance = AdminConferenceDetail.from_json(json)
# print the JSON string representation of the object
print(AdminConferenceDetail.to_json())

# convert the object into a dict
admin_conference_detail_dict = admin_conference_detail_instance.to_dict()
# create an instance of AdminConferenceDetail from a dict
admin_conference_detail_from_dict = AdminConferenceDetail.from_dict(admin_conference_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


