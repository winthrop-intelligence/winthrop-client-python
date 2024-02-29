# FinancialQc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**ncca_pdf** | **bool** |  | [optional] 
**audited_pdf** | **bool** |  | [optional] 
**nca_csv** | **bool** |  | [optional] 
**school_info_csv** | **bool** |  | [optional] 
**sport_stats_csv** | **bool** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.financial_qc import FinancialQc

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialQc from a JSON string
financial_qc_instance = FinancialQc.from_json(json)
# print the JSON string representation of the object
print FinancialQc.to_json()

# convert the object into a dict
financial_qc_dict = financial_qc_instance.to_dict()
# create an instance of FinancialQc from a dict
financial_qc_form_dict = financial_qc.from_dict(financial_qc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


