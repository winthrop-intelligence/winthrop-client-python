# AdminRequestedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foia_request_id** | **int** |  | [optional] 
**requestable_id** | **int** |  | [optional] 
**requestable_type** | **str** |  | [optional] 
**coach** | **str** | Coach name formatted as last name, first name | [optional] 
**coach_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**type_display** | **str** |  | [optional] 
**has_note** | **bool** |  | [optional] 
**foia_label** | **str** |  | [optional] 
**foia_state** | **str** |  | [optional] 
**foia_school** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_requested_item import AdminRequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRequestedItem from a JSON string
admin_requested_item_instance = AdminRequestedItem.from_json(json)
# print the JSON string representation of the object
print(AdminRequestedItem.to_json())

# convert the object into a dict
admin_requested_item_dict = admin_requested_item_instance.to_dict()
# create an instance of AdminRequestedItem from a dict
admin_requested_item_from_dict = AdminRequestedItem.from_dict(admin_requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


