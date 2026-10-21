# UpdateAdminConferenceshipsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conferenceship** | [**UpdateAdminConferenceshipsRequestConferenceship**](UpdateAdminConferenceshipsRequestConferenceship.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_conferenceships_request import UpdateAdminConferenceshipsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminConferenceshipsRequest from a JSON string
update_admin_conferenceships_request_instance = UpdateAdminConferenceshipsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminConferenceshipsRequest.to_json())

# convert the object into a dict
update_admin_conferenceships_request_dict = update_admin_conferenceships_request_instance.to_dict()
# create an instance of UpdateAdminConferenceshipsRequest from a dict
update_admin_conferenceships_request_from_dict = UpdateAdminConferenceshipsRequest.from_dict(update_admin_conferenceships_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


