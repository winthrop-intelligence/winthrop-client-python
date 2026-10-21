# AdminUserActivityInnerRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**tab** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_user_activity_inner_requests_inner import AdminUserActivityInnerRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserActivityInnerRequestsInner from a JSON string
admin_user_activity_inner_requests_inner_instance = AdminUserActivityInnerRequestsInner.from_json(json)
# print the JSON string representation of the object
print(AdminUserActivityInnerRequestsInner.to_json())

# convert the object into a dict
admin_user_activity_inner_requests_inner_dict = admin_user_activity_inner_requests_inner_instance.to_dict()
# create an instance of AdminUserActivityInnerRequestsInner from a dict
admin_user_activity_inner_requests_inner_from_dict = AdminUserActivityInnerRequestsInner.from_dict(admin_user_activity_inner_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


