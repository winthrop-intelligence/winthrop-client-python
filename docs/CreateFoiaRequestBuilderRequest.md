# CreateFoiaRequestBuilderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request_builder** | [**CreateFoiaRequestBuilderRequestFoiaRequestBuilder**](CreateFoiaRequestBuilderRequestFoiaRequestBuilder.md) |  | 

## Example

```python
from winthrop_client_python.models.create_foia_request_builder_request import CreateFoiaRequestBuilderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFoiaRequestBuilderRequest from a JSON string
create_foia_request_builder_request_instance = CreateFoiaRequestBuilderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFoiaRequestBuilderRequest.to_json())

# convert the object into a dict
create_foia_request_builder_request_dict = create_foia_request_builder_request_instance.to_dict()
# create an instance of CreateFoiaRequestBuilderRequest from a dict
create_foia_request_builder_request_from_dict = CreateFoiaRequestBuilderRequest.from_dict(create_foia_request_builder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


