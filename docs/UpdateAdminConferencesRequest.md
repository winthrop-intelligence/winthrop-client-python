# UpdateAdminConferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | [**UpdateAdminConferencesRequestConference**](UpdateAdminConferencesRequestConference.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_conferences_request import UpdateAdminConferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminConferencesRequest from a JSON string
update_admin_conferences_request_instance = UpdateAdminConferencesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminConferencesRequest.to_json())

# convert the object into a dict
update_admin_conferences_request_dict = update_admin_conferences_request_instance.to_dict()
# create an instance of UpdateAdminConferencesRequest from a dict
update_admin_conferences_request_from_dict = UpdateAdminConferencesRequest.from_dict(update_admin_conferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


