# UploadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[UploadItem]**](UploadItem.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.uploads_response import UploadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadsResponse from a JSON string
uploads_response_instance = UploadsResponse.from_json(json)
# print the JSON string representation of the object
print(UploadsResponse.to_json())

# convert the object into a dict
uploads_response_dict = uploads_response_instance.to_dict()
# create an instance of UploadsResponse from a dict
uploads_response_from_dict = UploadsResponse.from_dict(uploads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


