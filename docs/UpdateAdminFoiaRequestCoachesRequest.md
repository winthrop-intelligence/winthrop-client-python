# UpdateAdminFoiaRequestCoachesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request** | [**UpdateAdminFoiaRequestCoachesRequestFoiaRequest**](UpdateAdminFoiaRequestCoachesRequestFoiaRequest.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_foia_request_coaches_request import UpdateAdminFoiaRequestCoachesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFoiaRequestCoachesRequest from a JSON string
update_admin_foia_request_coaches_request_instance = UpdateAdminFoiaRequestCoachesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFoiaRequestCoachesRequest.to_json())

# convert the object into a dict
update_admin_foia_request_coaches_request_dict = update_admin_foia_request_coaches_request_instance.to_dict()
# create an instance of UpdateAdminFoiaRequestCoachesRequest from a dict
update_admin_foia_request_coaches_request_from_dict = UpdateAdminFoiaRequestCoachesRequest.from_dict(update_admin_foia_request_coaches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


