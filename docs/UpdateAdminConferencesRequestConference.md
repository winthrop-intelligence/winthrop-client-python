# UpdateAdminConferencesRequestConference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_subdivision_ids** | **List[int]** |  | [optional] 
**name_display** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**headquarters** | **str** |  | [optional] 
**founded** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**external_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_conferences_request_conference import UpdateAdminConferencesRequestConference

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminConferencesRequestConference from a JSON string
update_admin_conferences_request_conference_instance = UpdateAdminConferencesRequestConference.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminConferencesRequestConference.to_json())

# convert the object into a dict
update_admin_conferences_request_conference_dict = update_admin_conferences_request_conference_instance.to_dict()
# create an instance of UpdateAdminConferencesRequestConference from a dict
update_admin_conferences_request_conference_from_dict = UpdateAdminConferencesRequestConference.from_dict(update_admin_conferences_request_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


