# UpdateAdminFoiaRequestFinancialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request** | [**UpdateAdminFoiaRequestFinancialsRequestFoiaRequest**](UpdateAdminFoiaRequestFinancialsRequestFoiaRequest.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_foia_request_financials_request import UpdateAdminFoiaRequestFinancialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFoiaRequestFinancialsRequest from a JSON string
update_admin_foia_request_financials_request_instance = UpdateAdminFoiaRequestFinancialsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFoiaRequestFinancialsRequest.to_json())

# convert the object into a dict
update_admin_foia_request_financials_request_dict = update_admin_foia_request_financials_request_instance.to_dict()
# create an instance of UpdateAdminFoiaRequestFinancialsRequest from a dict
update_admin_foia_request_financials_request_from_dict = UpdateAdminFoiaRequestFinancialsRequest.from_dict(update_admin_foia_request_financials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


