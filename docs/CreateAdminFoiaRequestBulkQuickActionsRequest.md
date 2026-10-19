# CreateAdminFoiaRequestBulkQuickActionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_quick_actions** | [**CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions**](CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_foia_request_bulk_quick_actions_request import CreateAdminFoiaRequestBulkQuickActionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminFoiaRequestBulkQuickActionsRequest from a JSON string
create_admin_foia_request_bulk_quick_actions_request_instance = CreateAdminFoiaRequestBulkQuickActionsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminFoiaRequestBulkQuickActionsRequest.to_json())

# convert the object into a dict
create_admin_foia_request_bulk_quick_actions_request_dict = create_admin_foia_request_bulk_quick_actions_request_instance.to_dict()
# create an instance of CreateAdminFoiaRequestBulkQuickActionsRequest from a dict
create_admin_foia_request_bulk_quick_actions_request_from_dict = CreateAdminFoiaRequestBulkQuickActionsRequest.from_dict(create_admin_foia_request_bulk_quick_actions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


