# Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.meta import Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Meta from a JSON string
meta_instance = Meta.from_json(json)
# print the JSON string representation of the object
print(Meta.to_json())

# convert the object into a dict
meta_dict = meta_instance.to_dict()
# create an instance of Meta from a dict
meta_from_dict = Meta.from_dict(meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


