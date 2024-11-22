# VerifyUserIntercollegiateAccess200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_granted** | **bool** | Indicates whether the user has intercollegiate access | [optional] 

## Example

```python
from winthrop_client_python.models.verify_user_intercollegiate_access200_response import VerifyUserIntercollegiateAccess200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserIntercollegiateAccess200Response from a JSON string
verify_user_intercollegiate_access200_response_instance = VerifyUserIntercollegiateAccess200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyUserIntercollegiateAccess200Response.to_json())

# convert the object into a dict
verify_user_intercollegiate_access200_response_dict = verify_user_intercollegiate_access200_response_instance.to_dict()
# create an instance of VerifyUserIntercollegiateAccess200Response from a dict
verify_user_intercollegiate_access200_response_form_dict = verify_user_intercollegiate_access200_response.from_dict(verify_user_intercollegiate_access200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


