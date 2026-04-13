# GetTimeZones200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**us_zones** | [**List[TimeZoneOption]**](TimeZoneOption.md) |  | [optional] 
**other_zones** | [**List[TimeZoneOption]**](TimeZoneOption.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.get_time_zones200_response import GetTimeZones200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimeZones200Response from a JSON string
get_time_zones200_response_instance = GetTimeZones200Response.from_json(json)
# print the JSON string representation of the object
print(GetTimeZones200Response.to_json())

# convert the object into a dict
get_time_zones200_response_dict = get_time_zones200_response_instance.to_dict()
# create an instance of GetTimeZones200Response from a dict
get_time_zones200_response_from_dict = GetTimeZones200Response.from_dict(get_time_zones200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


