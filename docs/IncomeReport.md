# IncomeReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | 
**raw_contract_id** | **int** |  | 
**year** | **int** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 
**contract_status_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.income_report import IncomeReport

# TODO update the JSON string below
json = "{}"
# create an instance of IncomeReport from a JSON string
income_report_instance = IncomeReport.from_json(json)
# print the JSON string representation of the object
print IncomeReport.to_json()

# convert the object into a dict
income_report_dict = income_report_instance.to_dict()
# create an instance of IncomeReport from a dict
income_report_form_dict = income_report.from_dict(income_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


