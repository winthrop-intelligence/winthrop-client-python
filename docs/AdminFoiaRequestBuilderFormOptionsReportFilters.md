# AdminFoiaRequestBuilderFormOptionsReportFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schools** | [**List[AdminFoiaFilterOption]**](AdminFoiaFilterOption.md) |  | [optional] 
**conferences** | [**List[AdminFoiaFilterOption]**](AdminFoiaFilterOption.md) |  | [optional] 
**divisions** | [**List[AdminFoiaFilterOption]**](AdminFoiaFilterOption.md) |  | [optional] 
**subdivisions** | [**List[AdminFoiaFilterOption]**](AdminFoiaFilterOption.md) |  | [optional] 
**states** | [**List[AdminFoiaFilterOption]**](AdminFoiaFilterOption.md) |  | [optional] 
**labels** | [**List[AdminFoiaFilterOption]**](AdminFoiaFilterOption.md) |  | [optional] 
**contract_statuses** | [**List[AdminFoiaFilterOption]**](AdminFoiaFilterOption.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_builder_form_options_report_filters import AdminFoiaRequestBuilderFormOptionsReportFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestBuilderFormOptionsReportFilters from a JSON string
admin_foia_request_builder_form_options_report_filters_instance = AdminFoiaRequestBuilderFormOptionsReportFilters.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestBuilderFormOptionsReportFilters.to_json())

# convert the object into a dict
admin_foia_request_builder_form_options_report_filters_dict = admin_foia_request_builder_form_options_report_filters_instance.to_dict()
# create an instance of AdminFoiaRequestBuilderFormOptionsReportFilters from a dict
admin_foia_request_builder_form_options_report_filters_from_dict = AdminFoiaRequestBuilderFormOptionsReportFilters.from_dict(admin_foia_request_builder_form_options_report_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


