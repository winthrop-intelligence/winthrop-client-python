# ReconciliationPositionCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReconciliationPosition]**](ReconciliationPosition.md) |  | 
**meta** | [**ReconciliationPagination**](ReconciliationPagination.md) |  | 
**included** | [**ReconciliationIncluded**](ReconciliationIncluded.md) |  | 

## Example

```python
from winthrop_client_python.models.reconciliation_position_collection import ReconciliationPositionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationPositionCollection from a JSON string
reconciliation_position_collection_instance = ReconciliationPositionCollection.from_json(json)
# print the JSON string representation of the object
print(ReconciliationPositionCollection.to_json())

# convert the object into a dict
reconciliation_position_collection_dict = reconciliation_position_collection_instance.to_dict()
# create an instance of ReconciliationPositionCollection from a dict
reconciliation_position_collection_from_dict = ReconciliationPositionCollection.from_dict(reconciliation_position_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


