# FrsResolveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_mode** | **str** |  | 
**conference_id** | **int** |  | [optional] 
**school_group_id** | **int** |  | [optional] 
**financial_year** | **int** |  | 
**school_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.frs_resolve_request import FrsResolveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrsResolveRequest from a JSON string
frs_resolve_request_instance = FrsResolveRequest.from_json(json)
# print the JSON string representation of the object
print(FrsResolveRequest.to_json())

# convert the object into a dict
frs_resolve_request_dict = frs_resolve_request_instance.to_dict()
# create an instance of FrsResolveRequest from a dict
frs_resolve_request_from_dict = FrsResolveRequest.from_dict(frs_resolve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


