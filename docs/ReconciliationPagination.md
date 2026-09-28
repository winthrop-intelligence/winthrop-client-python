# ReconciliationPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | 
**total_pages** | **int** |  | 
**total_entries** | **int** |  | 
**next_page** | **int** |  | 
**previous_page** | **int** |  | 

## Example

```python
from winthrop_client_python.models.reconciliation_pagination import ReconciliationPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationPagination from a JSON string
reconciliation_pagination_instance = ReconciliationPagination.from_json(json)
# print the JSON string representation of the object
print(ReconciliationPagination.to_json())

# convert the object into a dict
reconciliation_pagination_dict = reconciliation_pagination_instance.to_dict()
# create an instance of ReconciliationPagination from a dict
reconciliation_pagination_from_dict = ReconciliationPagination.from_dict(reconciliation_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


