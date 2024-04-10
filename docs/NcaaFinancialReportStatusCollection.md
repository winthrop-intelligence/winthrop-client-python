# NcaaFinancialReportStatusCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NcaaFinancialReportStatus]**](NcaaFinancialReportStatus.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.ncaa_financial_report_status_collection import NcaaFinancialReportStatusCollection

# TODO update the JSON string below
json = "{}"
# create an instance of NcaaFinancialReportStatusCollection from a JSON string
ncaa_financial_report_status_collection_instance = NcaaFinancialReportStatusCollection.from_json(json)
# print the JSON string representation of the object
print(NcaaFinancialReportStatusCollection.to_json())

# convert the object into a dict
ncaa_financial_report_status_collection_dict = ncaa_financial_report_status_collection_instance.to_dict()
# create an instance of NcaaFinancialReportStatusCollection from a dict
ncaa_financial_report_status_collection_form_dict = ncaa_financial_report_status_collection.from_dict(ncaa_financial_report_status_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


