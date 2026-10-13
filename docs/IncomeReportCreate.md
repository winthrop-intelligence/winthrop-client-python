# IncomeReportCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | 
**raw_contract_id** | **int** | The attached document. Send null to detach it. A document can back only one income report; one already attached to another report is refused with 422 (errors.raw_contract_id). | [optional] 
**year** | **int** | Season end year (2011 &#x3D; the 2010-11 season). | 
**notes** | **str** |  | [optional] 
**contract_status_id** | **int** | Defaults to 1 on create. Attaching a document sets it to the complete status. | [optional] 
**change_note** | **str** | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

## Example

```python
from winthrop_client_python.models.income_report_create import IncomeReportCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IncomeReportCreate from a JSON string
income_report_create_instance = IncomeReportCreate.from_json(json)
# print the JSON string representation of the object
print(IncomeReportCreate.to_json())

# convert the object into a dict
income_report_create_dict = income_report_create_instance.to_dict()
# create an instance of IncomeReportCreate from a dict
income_report_create_from_dict = IncomeReportCreate.from_dict(income_report_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


