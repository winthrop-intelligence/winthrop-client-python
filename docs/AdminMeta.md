# AdminMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**comp_stats** | [**AdminMetaCompStats**](AdminMetaCompStats.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_meta import AdminMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminMeta from a JSON string
admin_meta_instance = AdminMeta.from_json(json)
# print the JSON string representation of the object
print(AdminMeta.to_json())

# convert the object into a dict
admin_meta_dict = admin_meta_instance.to_dict()
# create an instance of AdminMeta from a dict
admin_meta_from_dict = AdminMeta.from_dict(admin_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


