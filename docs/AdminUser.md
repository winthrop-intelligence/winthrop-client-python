# AdminUser

A single system user's full editable detail (admin namespace, cross-account)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**List[AdminUserActivityInner]**](AdminUserActivityInner.md) |  | [optional] 
**subscription** | [**AdminUserSubscription**](AdminUserSubscription.md) |  | [optional] 
**password_changed_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**otp_required** | **bool** |  | [optional] 
**otp_disabled_reason** | **str** |  | [optional] 
**do_not_send_invoice_emails** | **bool** |  | [optional] 
**scheduling_notifications** | **bool** |  | [optional] 
**game_post_notifications** | **bool** |  | [optional] 
**games_digest** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**directory_link** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**terms_accepted_at** | **datetime** |  | [optional] 
**confirmed_at** | **datetime** |  | [optional] 
**full_name** | **str** |  | [optional] 
**account** | [**AdminSchoolGroupAccount**](AdminSchoolGroupAccount.md) |  | [optional] 
**coach** | [**AdminUserCoach**](AdminUserCoach.md) |  | [optional] 
**role_symbols** | **List[str]** |  | [optional] 
**schedule_sport_ids** | **List[int]** |  | [optional] 
**schedule_sports** | [**List[IdName]**](IdName.md) |  | [optional] 
**permissible_sport_ids** | **List[int]** |  | [optional] 
**permissible_sports** | [**List[IdName]**](IdName.md) |  | [optional] 
**activity_count_last_180_days** | **int** |  | [optional] 
**created_by** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_user import AdminUser

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUser from a JSON string
admin_user_instance = AdminUser.from_json(json)
# print the JSON string representation of the object
print(AdminUser.to_json())

# convert the object into a dict
admin_user_dict = admin_user_instance.to_dict()
# create an instance of AdminUser from a dict
admin_user_from_dict = AdminUser.from_dict(admin_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


