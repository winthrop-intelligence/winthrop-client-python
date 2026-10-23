# AdminSystemSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**most_recent_apr_year** | **int** |  | [optional] 
**current_season_year** | **int** |  | [optional] 
**previous_season_year** | **int** |  | [optional] 
**current_financials_season_year** | **int** |  | [optional] 
**previous_financials_season_year** | **int** |  | [optional] 
**scheduling_target_year** | **int** | Automatic; not editable | 
**login_note** | **str** |  | [optional] 
**d1_projected_churn** | **float** |  | [optional] 
**d2_projected_churn** | **float** |  | [optional] 
**d1_price_dollars** | **str** | Decimal dollars, e.g. \&quot;15995.00\&quot; | [optional] 
**d2_price_dollars** | **str** |  | [optional] 
**d2_plus_price_dollars** | **str** |  | [optional] 
**coaches_and_administrators_price_dollars** | **str** |  | [optional] 
**license_agreement** | [**AdminSystemSettingLicenseAgreement**](AdminSystemSettingLicenseAgreement.md) |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_system_setting import AdminSystemSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSystemSetting from a JSON string
admin_system_setting_instance = AdminSystemSetting.from_json(json)
# print the JSON string representation of the object
print(AdminSystemSetting.to_json())

# convert the object into a dict
admin_system_setting_dict = admin_system_setting_instance.to_dict()
# create an instance of AdminSystemSetting from a dict
admin_system_setting_from_dict = AdminSystemSetting.from_dict(admin_system_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


