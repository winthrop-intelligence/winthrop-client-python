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
**outside_income_cents** | **int** | Total athletically related cash income the form reports, in cents. Send 0 when the form says no income and null to mark the form as not read. A negative, fractional or non-numeric value is refused with 422 (errors.outside_income_cents). | [optional] 
**reported_period** | **str** | The period exactly as the form states it, for example July 1, 2022 - June 30, 2023 or calendar 2022. Leading and trailing spaces are removed and a blank value is stored as null. A value that is not text or is longer than 255 characters is refused with 422 (errors.reported_period). | [optional] 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

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


