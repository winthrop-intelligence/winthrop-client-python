# FoiaInboxRequestedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item_id** | **int** |  | [optional] 
**requestable_type** | **str** |  | [optional] 
**requestable_id** | **int** |  | [optional] 
**type_display** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**ri_note_sha256** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**requestable_data** | [**FoiaInboxRequestableData**](FoiaInboxRequestableData.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_requested_item import FoiaInboxRequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxRequestedItem from a JSON string
foia_inbox_requested_item_instance = FoiaInboxRequestedItem.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxRequestedItem.to_json())

# convert the object into a dict
foia_inbox_requested_item_dict = foia_inbox_requested_item_instance.to_dict()
# create an instance of FoiaInboxRequestedItem from a dict
foia_inbox_requested_item_from_dict = FoiaInboxRequestedItem.from_dict(foia_inbox_requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


