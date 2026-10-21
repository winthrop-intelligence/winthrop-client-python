# AdminSchoolGroupAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**subscription_type** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_group_account import AdminSchoolGroupAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolGroupAccount from a JSON string
admin_school_group_account_instance = AdminSchoolGroupAccount.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolGroupAccount.to_json())

# convert the object into a dict
admin_school_group_account_dict = admin_school_group_account_instance.to_dict()
# create an instance of AdminSchoolGroupAccount from a dict
admin_school_group_account_from_dict = AdminSchoolGroupAccount.from_dict(admin_school_group_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


