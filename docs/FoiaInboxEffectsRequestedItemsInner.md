# FoiaInboxEffectsRequestedItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_effects_requested_items_inner import FoiaInboxEffectsRequestedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxEffectsRequestedItemsInner from a JSON string
foia_inbox_effects_requested_items_inner_instance = FoiaInboxEffectsRequestedItemsInner.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxEffectsRequestedItemsInner.to_json())

# convert the object into a dict
foia_inbox_effects_requested_items_inner_dict = foia_inbox_effects_requested_items_inner_instance.to_dict()
# create an instance of FoiaInboxEffectsRequestedItemsInner from a dict
foia_inbox_effects_requested_items_inner_from_dict = FoiaInboxEffectsRequestedItemsInner.from_dict(foia_inbox_effects_requested_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


