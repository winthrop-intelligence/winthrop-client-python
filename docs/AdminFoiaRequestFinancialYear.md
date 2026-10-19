# AdminFoiaRequestFinancialYear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**ncaa_financial_report_available** | **bool** |  | [optional] 
**ncaa_financial_report_filename** | **str** |  | [optional] 
**ncaa_status_id** | **int** |  | [optional] 
**ncaa_status_attached** | **bool** |  | [optional] 
**audited_financial_report_available** | **bool** |  | [optional] 
**audited_financial_report_filename** | **str** |  | [optional] 
**audited_status_label** | **str** |  | [optional] 
**audited_status_id** | **int** |  | [optional] 
**audited_status_attached** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_financial_year import AdminFoiaRequestFinancialYear

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestFinancialYear from a JSON string
admin_foia_request_financial_year_instance = AdminFoiaRequestFinancialYear.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestFinancialYear.to_json())

# convert the object into a dict
admin_foia_request_financial_year_dict = admin_foia_request_financial_year_instance.to_dict()
# create an instance of AdminFoiaRequestFinancialYear from a dict
admin_foia_request_financial_year_from_dict = AdminFoiaRequestFinancialYear.from_dict(admin_foia_request_financial_year_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


