# CreateUpload201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_upload201_response import CreateUpload201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpload201Response from a JSON string
create_upload201_response_instance = CreateUpload201Response.from_json(json)
# print the JSON string representation of the object
print(CreateUpload201Response.to_json())

# convert the object into a dict
create_upload201_response_dict = create_upload201_response_instance.to_dict()
# create an instance of CreateUpload201Response from a dict
create_upload201_response_from_dict = CreateUpload201Response.from_dict(create_upload201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


