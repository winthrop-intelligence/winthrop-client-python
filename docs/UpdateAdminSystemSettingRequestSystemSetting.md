# UpdateAdminSystemSettingRequestSystemSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**most_recent_apr_year** | **int** |  | [optional] 
**current_season_year** | **int** |  | [optional] 
**previous_season_year** | **int** |  | [optional] 
**current_financials_season_year** | **int** |  | [optional] 
**previous_financials_season_year** | **int** |  | [optional] 
**login_note** | **str** |  | [optional] 
**d1_projected_churn** | **float** |  | [optional] 
**d2_projected_churn** | **float** |  | [optional] 
**d1_price_dollars** | **str** | Decimal dollars, e.g. \&quot;15995.50\&quot;; blank clears the price | [optional] 
**d2_price_dollars** | **str** |  | [optional] 
**d2_plus_price_dollars** | **str** |  | [optional] 
**coaches_and_administrators_price_dollars** | **str** |  | [optional] 
**license_agreement** | **bytearray** | New standard license agreement; multipart only, and it must be a real PDF | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_system_setting_request_system_setting import UpdateAdminSystemSettingRequestSystemSetting

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminSystemSettingRequestSystemSetting from a JSON string
update_admin_system_setting_request_system_setting_instance = UpdateAdminSystemSettingRequestSystemSetting.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminSystemSettingRequestSystemSetting.to_json())

# convert the object into a dict
update_admin_system_setting_request_system_setting_dict = update_admin_system_setting_request_system_setting_instance.to_dict()
# create an instance of UpdateAdminSystemSettingRequestSystemSetting from a dict
update_admin_system_setting_request_system_setting_from_dict = UpdateAdminSystemSettingRequestSystemSetting.from_dict(update_admin_system_setting_request_system_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


