# AdminUserActivityInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**requests** | [**List[AdminUserActivityInnerRequestsInner]**](AdminUserActivityInnerRequestsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_user_activity_inner import AdminUserActivityInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserActivityInner from a JSON string
admin_user_activity_inner_instance = AdminUserActivityInner.from_json(json)
# print the JSON string representation of the object
print(AdminUserActivityInner.to_json())

# convert the object into a dict
admin_user_activity_inner_dict = admin_user_activity_inner_instance.to_dict()
# create an instance of AdminUserActivityInner from a dict
admin_user_activity_inner_from_dict = AdminUserActivityInner.from_dict(admin_user_activity_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


