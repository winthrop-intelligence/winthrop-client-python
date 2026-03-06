# CompStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**average** | **int** |  | [optional] 
**median** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.comp_stats import CompStats

# TODO update the JSON string below
json = "{}"
# create an instance of CompStats from a JSON string
comp_stats_instance = CompStats.from_json(json)
# print the JSON string representation of the object
print(CompStats.to_json())

# convert the object into a dict
comp_stats_dict = comp_stats_instance.to_dict()
# create an instance of CompStats from a dict
comp_stats_from_dict = CompStats.from_dict(comp_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


