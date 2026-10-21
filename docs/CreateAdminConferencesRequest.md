# CreateAdminConferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | [**CreateAdminConferencesRequestConference**](CreateAdminConferencesRequestConference.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_conferences_request import CreateAdminConferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminConferencesRequest from a JSON string
create_admin_conferences_request_instance = CreateAdminConferencesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminConferencesRequest.to_json())

# convert the object into a dict
create_admin_conferences_request_dict = create_admin_conferences_request_instance.to_dict()
# create an instance of CreateAdminConferencesRequest from a dict
create_admin_conferences_request_from_dict = CreateAdminConferencesRequest.from_dict(create_admin_conferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


