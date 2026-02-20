# GetFilterOptions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**years** | **List[int]** |  | [optional] 
**current_year** | **int** |  | [optional] 
**divisions** | [**List[IdName]**](IdName.md) |  | [optional] 
**sports** | [**List[IdName]**](IdName.md) |  | [optional] 
**position_types** | [**List[IdName]**](IdName.md) |  | [optional] 
**geo_regions** | [**List[IdName]**](IdName.md) |  | [optional] 
**gender_options** | **List[str]** |  | [optional] 
**diversity_options** | **List[str]** |  | [optional] 
**compensation_types** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.get_filter_options200_response import GetFilterOptions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFilterOptions200Response from a JSON string
get_filter_options200_response_instance = GetFilterOptions200Response.from_json(json)
# print the JSON string representation of the object
print(GetFilterOptions200Response.to_json())

# convert the object into a dict
get_filter_options200_response_dict = get_filter_options200_response_instance.to_dict()
# create an instance of GetFilterOptions200Response from a dict
get_filter_options200_response_from_dict = GetFilterOptions200Response.from_dict(get_filter_options200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


