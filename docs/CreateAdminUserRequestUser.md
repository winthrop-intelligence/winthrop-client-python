# CreateAdminUserRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**otp_disabled_reason** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**password_confirmation** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**directory_link** | **str** |  | [optional] 
**otp_required** | **bool** |  | [optional] 
**do_not_send_invoice_emails** | **bool** |  | [optional] 
**scheduling_notifications** | **bool** |  | [optional] 
**game_post_notifications** | **bool** |  | [optional] 
**games_digest** | **bool** |  | [optional] 
**no_profile** | **bool** |  | [optional] 
**account_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**role_symbols** | **List[str]** |  | [optional] 
**schedule_sport_ids** | **List[int]** |  | [optional] 
**permissible_sport_ids** | **List[int]** |  | [optional] 
**skip_confirmation** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_user_request_user import CreateAdminUserRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminUserRequestUser from a JSON string
create_admin_user_request_user_instance = CreateAdminUserRequestUser.from_json(json)
# print the JSON string representation of the object
print(CreateAdminUserRequestUser.to_json())

# convert the object into a dict
create_admin_user_request_user_dict = create_admin_user_request_user_instance.to_dict()
# create an instance of CreateAdminUserRequestUser from a dict
create_admin_user_request_user_from_dict = CreateAdminUserRequestUser.from_dict(create_admin_user_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


