# DepartmentGuaranteesSportLedger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | 
**sport_key** | **str** |  | 
**sport_name** | **str** |  | 
**agreement_count** | **int** |  | 
**out_count** | **int** |  | 
**out_total_cents** | **int** |  | 
**out_median_cents** | **int** |  | 
**agreements** | [**List[DepartmentGuaranteesAgreement]**](DepartmentGuaranteesAgreement.md) |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_sport_ledger import DepartmentGuaranteesSportLedger

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesSportLedger from a JSON string
department_guarantees_sport_ledger_instance = DepartmentGuaranteesSportLedger.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesSportLedger.to_json())

# convert the object into a dict
department_guarantees_sport_ledger_dict = department_guarantees_sport_ledger_instance.to_dict()
# create an instance of DepartmentGuaranteesSportLedger from a dict
department_guarantees_sport_ledger_from_dict = DepartmentGuaranteesSportLedger.from_dict(department_guarantees_sport_ledger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


