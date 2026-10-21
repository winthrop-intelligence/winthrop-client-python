# AdminSchoolDetailFinancialReportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**ncaa** | **str** |  | [optional] 
**audited** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_detail_financial_reports_inner import AdminSchoolDetailFinancialReportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolDetailFinancialReportsInner from a JSON string
admin_school_detail_financial_reports_inner_instance = AdminSchoolDetailFinancialReportsInner.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolDetailFinancialReportsInner.to_json())

# convert the object into a dict
admin_school_detail_financial_reports_inner_dict = admin_school_detail_financial_reports_inner_instance.to_dict()
# create an instance of AdminSchoolDetailFinancialReportsInner from a dict
admin_school_detail_financial_reports_inner_from_dict = AdminSchoolDetailFinancialReportsInner.from_dict(admin_school_detail_financial_reports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


