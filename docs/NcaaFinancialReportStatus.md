# NcaaFinancialReportStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**available** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.ncaa_financial_report_status import NcaaFinancialReportStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NcaaFinancialReportStatus from a JSON string
ncaa_financial_report_status_instance = NcaaFinancialReportStatus.from_json(json)
# print the JSON string representation of the object
print NcaaFinancialReportStatus.to_json()

# convert the object into a dict
ncaa_financial_report_status_dict = ncaa_financial_report_status_instance.to_dict()
# create an instance of NcaaFinancialReportStatus from a dict
ncaa_financial_report_status_form_dict = ncaa_financial_report_status.from_dict(ncaa_financial_report_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


