# TimeZoneOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Time zone identifier (e.g. \&quot;Eastern Time (US &amp; Canada)\&quot;) | [optional] 
**label** | **str** | Display label with GMT offset (e.g. \&quot;(GMT-05:00) Eastern Time (US &amp; Canada)\&quot;) | [optional] 

## Example

```python
from winthrop_client_python.models.time_zone_option import TimeZoneOption

# TODO update the JSON string below
json = "{}"
# create an instance of TimeZoneOption from a JSON string
time_zone_option_instance = TimeZoneOption.from_json(json)
# print the JSON string representation of the object
print(TimeZoneOption.to_json())

# convert the object into a dict
time_zone_option_dict = time_zone_option_instance.to_dict()
# create an instance of TimeZoneOption from a dict
time_zone_option_from_dict = TimeZoneOption.from_dict(time_zone_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


