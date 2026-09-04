# DeskRequestsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**DeskReportsResponseMeta**](DeskReportsResponseMeta.md) |  | 
**data** | [**List[DeskRequest]**](DeskRequest.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_requests_response import DeskRequestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskRequestsResponse from a JSON string
desk_requests_response_instance = DeskRequestsResponse.from_json(json)
# print the JSON string representation of the object
print(DeskRequestsResponse.to_json())

# convert the object into a dict
desk_requests_response_dict = desk_requests_response_instance.to_dict()
# create an instance of DeskRequestsResponse from a dict
desk_requests_response_from_dict = DeskRequestsResponse.from_dict(desk_requests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


