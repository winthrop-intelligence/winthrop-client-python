# CompensationClosureResponseCompensation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**contract_status** | **str** |  | 
**comment** | **str** |  | 
**positions** | [**List[CompensationClosureResponseCompensationPositionsInner]**](CompensationClosureResponseCompensationPositionsInner.md) |  | 

## Example

```python
from winthrop_client_python.models.compensation_closure_response_compensation import CompensationClosureResponseCompensation

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationClosureResponseCompensation from a JSON string
compensation_closure_response_compensation_instance = CompensationClosureResponseCompensation.from_json(json)
# print the JSON string representation of the object
print(CompensationClosureResponseCompensation.to_json())

# convert the object into a dict
compensation_closure_response_compensation_dict = compensation_closure_response_compensation_instance.to_dict()
# create an instance of CompensationClosureResponseCompensation from a dict
compensation_closure_response_compensation_from_dict = CompensationClosureResponseCompensation.from_dict(compensation_closure_response_compensation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


