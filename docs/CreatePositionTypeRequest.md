# CreatePositionTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_type** | [**CreatePositionTypeRequestPositionType**](CreatePositionTypeRequestPositionType.md) |  | 

## Example

```python
from winthrop_client_python.models.create_position_type_request import CreatePositionTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePositionTypeRequest from a JSON string
create_position_type_request_instance = CreatePositionTypeRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePositionTypeRequest.to_json())

# convert the object into a dict
create_position_type_request_dict = create_position_type_request_instance.to_dict()
# create an instance of CreatePositionTypeRequest from a dict
create_position_type_request_from_dict = CreatePositionTypeRequest.from_dict(create_position_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


