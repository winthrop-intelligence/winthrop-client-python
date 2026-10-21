# CreateAdminConferencesRequestConference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_display** | **str** |  | 
**nickname** | **str** |  | [optional] 
**headquarters** | **str** |  | [optional] 
**founded** | **int** |  | [optional] 
**division_id** | **int** |  | [optional] 
**external_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_conferences_request_conference import CreateAdminConferencesRequestConference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminConferencesRequestConference from a JSON string
create_admin_conferences_request_conference_instance = CreateAdminConferencesRequestConference.from_json(json)
# print the JSON string representation of the object
print(CreateAdminConferencesRequestConference.to_json())

# convert the object into a dict
create_admin_conferences_request_conference_dict = create_admin_conferences_request_conference_instance.to_dict()
# create an instance of CreateAdminConferencesRequestConference from a dict
create_admin_conferences_request_conference_from_dict = CreateAdminConferencesRequestConference.from_dict(create_admin_conferences_request_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


