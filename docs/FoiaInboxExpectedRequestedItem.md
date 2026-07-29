# FoiaInboxExpectedRequestedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**updated_at** | **datetime** |  | 
**ri_note_sha256** | **str** |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_expected_requested_item import FoiaInboxExpectedRequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxExpectedRequestedItem from a JSON string
foia_inbox_expected_requested_item_instance = FoiaInboxExpectedRequestedItem.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxExpectedRequestedItem.to_json())

# convert the object into a dict
foia_inbox_expected_requested_item_dict = foia_inbox_expected_requested_item_instance.to_dict()
# create an instance of FoiaInboxExpectedRequestedItem from a dict
foia_inbox_expected_requested_item_from_dict = FoiaInboxExpectedRequestedItem.from_dict(foia_inbox_expected_requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


