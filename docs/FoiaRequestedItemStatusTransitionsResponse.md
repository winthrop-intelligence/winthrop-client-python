# FoiaRequestedItemStatusTransitionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**FoiaRequestedItemStatusTransitionsMeta**](FoiaRequestedItemStatusTransitionsMeta.md) |  | [optional] 
**data** | [**List[FoiaRequestedItemStatusTransitionRow]**](FoiaRequestedItemStatusTransitionRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_requested_item_status_transitions_response import FoiaRequestedItemStatusTransitionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestedItemStatusTransitionsResponse from a JSON string
foia_requested_item_status_transitions_response_instance = FoiaRequestedItemStatusTransitionsResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestedItemStatusTransitionsResponse.to_json())

# convert the object into a dict
foia_requested_item_status_transitions_response_dict = foia_requested_item_status_transitions_response_instance.to_dict()
# create an instance of FoiaRequestedItemStatusTransitionsResponse from a dict
foia_requested_item_status_transitions_response_from_dict = FoiaRequestedItemStatusTransitionsResponse.from_dict(foia_requested_item_status_transitions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


