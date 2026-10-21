# AdminUserSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**start_at** | **str** |  | [optional] 
**end_at** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_user_subscription import AdminUserSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserSubscription from a JSON string
admin_user_subscription_instance = AdminUserSubscription.from_json(json)
# print the JSON string representation of the object
print(AdminUserSubscription.to_json())

# convert the object into a dict
admin_user_subscription_dict = admin_user_subscription_instance.to_dict()
# create an instance of AdminUserSubscription from a dict
admin_user_subscription_from_dict = AdminUserSubscription.from_dict(admin_user_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


