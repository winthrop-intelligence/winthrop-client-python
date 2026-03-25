# AdministratorSearchResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Administrator]**](Administrator.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**comp_stats** | [**CompStats**](CompStats.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.administrator_search_result_collection import AdministratorSearchResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of AdministratorSearchResultCollection from a JSON string
administrator_search_result_collection_instance = AdministratorSearchResultCollection.from_json(json)
# print the JSON string representation of the object
print(AdministratorSearchResultCollection.to_json())

# convert the object into a dict
administrator_search_result_collection_dict = administrator_search_result_collection_instance.to_dict()
# create an instance of AdministratorSearchResultCollection from a dict
administrator_search_result_collection_from_dict = AdministratorSearchResultCollection.from_dict(administrator_search_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


