# TimeOfYearOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name_display** | **str** |  | 

## Example

```python
from winthrop_client_python.models.time_of_year_option import TimeOfYearOption

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOfYearOption from a JSON string
time_of_year_option_instance = TimeOfYearOption.from_json(json)
# print the JSON string representation of the object
print(TimeOfYearOption.to_json())

# convert the object into a dict
time_of_year_option_dict = time_of_year_option_instance.to_dict()
# create an instance of TimeOfYearOption from a dict
time_of_year_option_from_dict = TimeOfYearOption.from_dict(time_of_year_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


