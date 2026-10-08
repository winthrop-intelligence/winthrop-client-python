# IncomeReportInput

Fields for POST/PATCH /income_reports, sent at the top level of the JSON body beside change_note. PATCH changes only the fields sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**raw_contract_id** | **int** | The attached document. Send null to detach it. A document can back only one income report; one already attached to another report is refused with 422 (errors.raw_contract_id). | [optional] 
**year** | **int** | Season end year (2011 &#x3D; the 2010-11 season). | [optional] 
**notes** | **str** |  | [optional] 
**contract_status_id** | **int** | Defaults to 1 on create. Attaching a document sets it to the complete status. | [optional] 
**change_note** | **str** | Why this change is being made, for the internal audit history (WINAD-10625). It is stored on the audit version this write creates and is never returned. Blank is the same as omitted; a non-string value is refused with 422 (errors.change_note). | [optional] 

## Example

```python
from winthrop_client_python.models.income_report_input import IncomeReportInput

# TODO update the JSON string below
json = "{}"
# create an instance of IncomeReportInput from a JSON string
income_report_input_instance = IncomeReportInput.from_json(json)
# print the JSON string representation of the object
print(IncomeReportInput.to_json())

# convert the object into a dict
income_report_input_dict = income_report_input_instance.to_dict()
# create an instance of IncomeReportInput from a dict
income_report_input_from_dict = IncomeReportInput.from_dict(income_report_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


