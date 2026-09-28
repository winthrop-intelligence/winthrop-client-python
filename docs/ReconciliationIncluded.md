# ReconciliationIncluded

Only entities referenced by this page, each once and ordered by ID. Missing associations have no entry; clients must tolerate unresolved nullable IDs. Empty result pages contain four empty arrays.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coaches** | [**List[ReconciliationCoach]**](ReconciliationCoach.md) |  | 
**schools** | [**List[ReconciliationSchool]**](ReconciliationSchool.md) |  | 
**sports** | [**List[ReconciliationSport]**](ReconciliationSport.md) |  | 
**position_types** | [**List[ReconciliationPositionType]**](ReconciliationPositionType.md) |  | 

## Example

```python
from winthrop_client_python.models.reconciliation_included import ReconciliationIncluded

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationIncluded from a JSON string
reconciliation_included_instance = ReconciliationIncluded.from_json(json)
# print the JSON string representation of the object
print(ReconciliationIncluded.to_json())

# convert the object into a dict
reconciliation_included_dict = reconciliation_included_instance.to_dict()
# create an instance of ReconciliationIncluded from a dict
reconciliation_included_from_dict = ReconciliationIncluded.from_dict(reconciliation_included_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


