# GadSearchStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** |  | [optional] 
**min_cents** | **int** |  | [optional] 
**max_cents** | **int** |  | [optional] 
**average_cents** | **int** |  | [optional] 
**median_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.gad_search_stats import GadSearchStats

# TODO update the JSON string below
json = "{}"
# create an instance of GadSearchStats from a JSON string
gad_search_stats_instance = GadSearchStats.from_json(json)
# print the JSON string representation of the object
print(GadSearchStats.to_json())

# convert the object into a dict
gad_search_stats_dict = gad_search_stats_instance.to_dict()
# create an instance of GadSearchStats from a dict
gad_search_stats_from_dict = GadSearchStats.from_dict(gad_search_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


