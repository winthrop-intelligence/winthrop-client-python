# DepartmentGuaranteesAgreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_contract_id** | **int** |  | 
**direction** | **str** |  | 
**opponent** | [**DepartmentGuaranteesAgreementOpponent**](DepartmentGuaranteesAgreementOpponent.md) |  | 
**game_date** | **date** |  | 
**game_date_tbd** | **str** |  | 
**comp_cents** | **int** |  | 
**comp_tbd** | **bool** |  | 
**has_document** | **bool** |  | 
**belongs_to_series** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_agreement import DepartmentGuaranteesAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesAgreement from a JSON string
department_guarantees_agreement_instance = DepartmentGuaranteesAgreement.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesAgreement.to_json())

# convert the object into a dict
department_guarantees_agreement_dict = department_guarantees_agreement_instance.to_dict()
# create an instance of DepartmentGuaranteesAgreement from a dict
department_guarantees_agreement_from_dict = DepartmentGuaranteesAgreement.from_dict(department_guarantees_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


