# AdminFoiaRequestBuilderFormOptions

Selectable schools/sports/compensation options for the FOIA Request Builder form

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**sports** | [**List[IdName]**](IdName.md) |  | [optional] 
**report_filters** | [**AdminFoiaRequestBuilderFormOptionsReportFilters**](AdminFoiaRequestBuilderFormOptionsReportFilters.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_builder_form_options import AdminFoiaRequestBuilderFormOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestBuilderFormOptions from a JSON string
admin_foia_request_builder_form_options_instance = AdminFoiaRequestBuilderFormOptions.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestBuilderFormOptions.to_json())

# convert the object into a dict
admin_foia_request_builder_form_options_dict = admin_foia_request_builder_form_options_instance.to_dict()
# create an instance of AdminFoiaRequestBuilderFormOptions from a dict
admin_foia_request_builder_form_options_from_dict = AdminFoiaRequestBuilderFormOptions.from_dict(admin_foia_request_builder_form_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


