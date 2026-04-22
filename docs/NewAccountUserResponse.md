# NewAccountUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_domain** | **str** |  | [optional] 
**role_options** | [**List[RoleOption]**](RoleOption.md) |  | [optional] 
**schedulable_sports** | [**List[SportOption]**](SportOption.md) |  | [optional] 
**all_sports** | [**List[SportOption]**](SportOption.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.new_account_user_response import NewAccountUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewAccountUserResponse from a JSON string
new_account_user_response_instance = NewAccountUserResponse.from_json(json)
# print the JSON string representation of the object
print(NewAccountUserResponse.to_json())

# convert the object into a dict
new_account_user_response_dict = new_account_user_response_instance.to_dict()
# create an instance of NewAccountUserResponse from a dict
new_account_user_response_from_dict = NewAccountUserResponse.from_dict(new_account_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


