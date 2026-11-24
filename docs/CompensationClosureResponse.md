# CompensationClosureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**actor_id** | **int** | User recorded as having made the change | 
**requested_item** | [**CompensationClosureResponseRequestedItem**](CompensationClosureResponseRequestedItem.md) |  | 
**compensation** | [**CompensationClosureResponseCompensation**](CompensationClosureResponseCompensation.md) |  | 

## Example

```python
from winthrop_client_python.models.compensation_closure_response import CompensationClosureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationClosureResponse from a JSON string
compensation_closure_response_instance = CompensationClosureResponse.from_json(json)
# print the JSON string representation of the object
print(CompensationClosureResponse.to_json())

# convert the object into a dict
compensation_closure_response_dict = compensation_closure_response_instance.to_dict()
# create an instance of CompensationClosureResponse from a dict
compensation_closure_response_from_dict = CompensationClosureResponse.from_dict(compensation_closure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


