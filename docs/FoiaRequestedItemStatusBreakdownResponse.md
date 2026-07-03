# FoiaRequestedItemStatusBreakdownResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**FoiaRequestedItemStatusBreakdownMeta**](FoiaRequestedItemStatusBreakdownMeta.md) |  | [optional] 
**data** | [**List[FoiaRequestedItemStatusBreakdownRow]**](FoiaRequestedItemStatusBreakdownRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_requested_item_status_breakdown_response import FoiaRequestedItemStatusBreakdownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestedItemStatusBreakdownResponse from a JSON string
foia_requested_item_status_breakdown_response_instance = FoiaRequestedItemStatusBreakdownResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestedItemStatusBreakdownResponse.to_json())

# convert the object into a dict
foia_requested_item_status_breakdown_response_dict = foia_requested_item_status_breakdown_response_instance.to_dict()
# create an instance of FoiaRequestedItemStatusBreakdownResponse from a dict
foia_requested_item_status_breakdown_response_from_dict = FoiaRequestedItemStatusBreakdownResponse.from_dict(foia_requested_item_status_breakdown_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


