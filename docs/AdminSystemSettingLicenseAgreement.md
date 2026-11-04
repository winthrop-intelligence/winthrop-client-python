# AdminSystemSettingLicenseAgreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**filename** | **str** |  | 
**url** | **str** | Active Storage path of the file | 

## Example

```python
from winthrop_client_python.models.admin_system_setting_license_agreement import AdminSystemSettingLicenseAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSystemSettingLicenseAgreement from a JSON string
admin_system_setting_license_agreement_instance = AdminSystemSettingLicenseAgreement.from_json(json)
# print the JSON string representation of the object
print(AdminSystemSettingLicenseAgreement.to_json())

# convert the object into a dict
admin_system_setting_license_agreement_dict = admin_system_setting_license_agreement_instance.to_dict()
# create an instance of AdminSystemSettingLicenseAgreement from a dict
admin_system_setting_license_agreement_from_dict = AdminSystemSettingLicenseAgreement.from_dict(admin_system_setting_license_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


