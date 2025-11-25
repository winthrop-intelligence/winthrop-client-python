# GetWireChanges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**wire_changes** | [**List[WireChange]**](WireChange.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.get_wire_changes200_response import GetWireChanges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWireChanges200Response from a JSON string
get_wire_changes200_response_instance = GetWireChanges200Response.from_json(json)
# print the JSON string representation of the object
print(GetWireChanges200Response.to_json())

# convert the object into a dict
get_wire_changes200_response_dict = get_wire_changes200_response_instance.to_dict()
# create an instance of GetWireChanges200Response from a dict
get_wire_changes200_response_from_dict = GetWireChanges200Response.from_dict(get_wire_changes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


