# GetLadFilterOptions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_types** | [**List[IdName]**](IdName.md) |  | [optional] 
**departments** | [**List[IdName]**](IdName.md) |  | [optional] 
**school_groups** | [**List[IdName]**](IdName.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.get_lad_filter_options200_response import GetLadFilterOptions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLadFilterOptions200Response from a JSON string
get_lad_filter_options200_response_instance = GetLadFilterOptions200Response.from_json(json)
# print the JSON string representation of the object
print(GetLadFilterOptions200Response.to_json())

# convert the object into a dict
get_lad_filter_options200_response_dict = get_lad_filter_options200_response_instance.to_dict()
# create an instance of GetLadFilterOptions200Response from a dict
get_lad_filter_options200_response_from_dict = GetLadFilterOptions200Response.from_dict(get_lad_filter_options200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


