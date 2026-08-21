# CreateDeskRequest201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeskRequest**](DeskRequest.md) |  | 

## Example

```python
from winthrop_client_python.models.create_desk_request201_response import CreateDeskRequest201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeskRequest201Response from a JSON string
create_desk_request201_response_instance = CreateDeskRequest201Response.from_json(json)
# print the JSON string representation of the object
print(CreateDeskRequest201Response.to_json())

# convert the object into a dict
create_desk_request201_response_dict = create_desk_request201_response_instance.to_dict()
# create an instance of CreateDeskRequest201Response from a dict
create_desk_request201_response_from_dict = CreateDeskRequest201Response.from_dict(create_desk_request201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


