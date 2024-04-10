# RequestedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foia_request_id** | **int** |  | 
**requestable_id** | **int** |  | 
**requestable_type** | **str** |  | 
**received** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.requested_item import RequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItem from a JSON string
requested_item_instance = RequestedItem.from_json(json)
# print the JSON string representation of the object
print(RequestedItem.to_json())

# convert the object into a dict
requested_item_dict = requested_item_instance.to_dict()
# create an instance of RequestedItem from a dict
requested_item_form_dict = requested_item.from_dict(requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


