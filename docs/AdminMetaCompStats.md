# AdminMetaCompStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**average** | **int** |  | [optional] 
**median** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_meta_comp_stats import AdminMetaCompStats

# TODO update the JSON string below
json = "{}"
# create an instance of AdminMetaCompStats from a JSON string
admin_meta_comp_stats_instance = AdminMetaCompStats.from_json(json)
# print the JSON string representation of the object
print(AdminMetaCompStats.to_json())

# convert the object into a dict
admin_meta_comp_stats_dict = admin_meta_comp_stats_instance.to_dict()
# create an instance of AdminMetaCompStats from a dict
admin_meta_comp_stats_from_dict = AdminMetaCompStats.from_dict(admin_meta_comp_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


