# ReconciliationCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**bio** | **str** | Biography URL, never biography text. | 

## Example

```python
from winthrop_client_python.models.reconciliation_coach import ReconciliationCoach

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationCoach from a JSON string
reconciliation_coach_instance = ReconciliationCoach.from_json(json)
# print the JSON string representation of the object
print(ReconciliationCoach.to_json())

# convert the object into a dict
reconciliation_coach_dict = reconciliation_coach_instance.to_dict()
# create an instance of ReconciliationCoach from a dict
reconciliation_coach_from_dict = ReconciliationCoach.from_dict(reconciliation_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


