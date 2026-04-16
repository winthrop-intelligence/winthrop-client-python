# AccountUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**AccountInfo**](AccountInfo.md) |  | [optional] 
**users** | [**List[AccountUser]**](AccountUser.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.account_users_response import AccountUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUsersResponse from a JSON string
account_users_response_instance = AccountUsersResponse.from_json(json)
# print the JSON string representation of the object
print(AccountUsersResponse.to_json())

# convert the object into a dict
account_users_response_dict = account_users_response_instance.to_dict()
# create an instance of AccountUsersResponse from a dict
account_users_response_from_dict = AccountUsersResponse.from_dict(account_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


