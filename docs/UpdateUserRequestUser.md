# UpdateUserRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**scheduling_notifications** | **bool** |  | [optional] 
**game_post_notifications** | **bool** |  | [optional] 
**games_digest** | **bool** |  | [optional] 
**current_password** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**password_confirmation** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_user_request_user import UpdateUserRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestUser from a JSON string
update_user_request_user_instance = UpdateUserRequestUser.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestUser.to_json())

# convert the object into a dict
update_user_request_user_dict = update_user_request_user_instance.to_dict()
# create an instance of UpdateUserRequestUser from a dict
update_user_request_user_from_dict = UpdateUserRequestUser.from_dict(update_user_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


