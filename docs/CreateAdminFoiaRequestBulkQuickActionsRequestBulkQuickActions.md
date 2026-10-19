# CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**requested_item_ids** | **List[int]** |  | [optional] 
**actions** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_foia_request_bulk_quick_actions_request_bulk_quick_actions import CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions from a JSON string
create_admin_foia_request_bulk_quick_actions_request_bulk_quick_actions_instance = CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions.from_json(json)
# print the JSON string representation of the object
print(CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions.to_json())

# convert the object into a dict
create_admin_foia_request_bulk_quick_actions_request_bulk_quick_actions_dict = create_admin_foia_request_bulk_quick_actions_request_bulk_quick_actions_instance.to_dict()
# create an instance of CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions from a dict
create_admin_foia_request_bulk_quick_actions_request_bulk_quick_actions_from_dict = CreateAdminFoiaRequestBulkQuickActionsRequestBulkQuickActions.from_dict(create_admin_foia_request_bulk_quick_actions_request_bulk_quick_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


