# ReconciliationPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**coach_id** | **int** |  | 
**season_id** | **int** |  | 
**season_year** | **int** |  | 
**school_id** | **int** |  | 
**sport_id** | **int** |  | 
**title** | **str** |  | 
**departing** | **bool** |  | 
**position_type_ids** | **List[int]** |  | 

## Example

```python
from winthrop_client_python.models.reconciliation_position import ReconciliationPosition

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationPosition from a JSON string
reconciliation_position_instance = ReconciliationPosition.from_json(json)
# print the JSON string representation of the object
print(ReconciliationPosition.to_json())

# convert the object into a dict
reconciliation_position_dict = reconciliation_position_instance.to_dict()
# create an instance of ReconciliationPosition from a dict
reconciliation_position_from_dict = ReconciliationPosition.from_dict(reconciliation_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


