# ReconciliationSport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**name_display** | **str** |  | 

## Example

```python
from winthrop_client_python.models.reconciliation_sport import ReconciliationSport

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationSport from a JSON string
reconciliation_sport_instance = ReconciliationSport.from_json(json)
# print the JSON string representation of the object
print(ReconciliationSport.to_json())

# convert the object into a dict
reconciliation_sport_dict = reconciliation_sport_instance.to_dict()
# create an instance of ReconciliationSport from a dict
reconciliation_sport_from_dict = ReconciliationSport.from_dict(reconciliation_sport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


