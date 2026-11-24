# CompensationClosureResponseRequestedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | **str** |  | 
**note** | **str** |  | 

## Example

```python
from winthrop_client_python.models.compensation_closure_response_requested_item import CompensationClosureResponseRequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationClosureResponseRequestedItem from a JSON string
compensation_closure_response_requested_item_instance = CompensationClosureResponseRequestedItem.from_json(json)
# print the JSON string representation of the object
print(CompensationClosureResponseRequestedItem.to_json())

# convert the object into a dict
compensation_closure_response_requested_item_dict = compensation_closure_response_requested_item_instance.to_dict()
# create an instance of CompensationClosureResponseRequestedItem from a dict
compensation_closure_response_requested_item_from_dict = CompensationClosureResponseRequestedItem.from_dict(compensation_closure_response_requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


