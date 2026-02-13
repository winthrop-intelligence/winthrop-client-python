# DepartmentSearchResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DepartmentSearchResult]**](DepartmentSearchResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.department_search_result_collection import DepartmentSearchResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentSearchResultCollection from a JSON string
department_search_result_collection_instance = DepartmentSearchResultCollection.from_json(json)
# print the JSON string representation of the object
print(DepartmentSearchResultCollection.to_json())

# convert the object into a dict
department_search_result_collection_dict = department_search_result_collection_instance.to_dict()
# create an instance of DepartmentSearchResultCollection from a dict
department_search_result_collection_from_dict = DepartmentSearchResultCollection.from_dict(department_search_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


