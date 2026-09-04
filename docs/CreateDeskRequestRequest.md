# CreateDeskRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 
**category** | **str** |  | [optional] 
**source_report_uuid** | **str** |  | [optional] 
**cta_key** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_desk_request_request import CreateDeskRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeskRequestRequest from a JSON string
create_desk_request_request_instance = CreateDeskRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDeskRequestRequest.to_json())

# convert the object into a dict
create_desk_request_request_dict = create_desk_request_request_instance.to_dict()
# create an instance of CreateDeskRequestRequest from a dict
create_desk_request_request_from_dict = CreateDeskRequestRequest.from_dict(create_desk_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


