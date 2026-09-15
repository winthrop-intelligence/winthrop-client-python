# DeskAdminReportsResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.desk_admin_reports_response_meta import DeskAdminReportsResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminReportsResponseMeta from a JSON string
desk_admin_reports_response_meta_instance = DeskAdminReportsResponseMeta.from_json(json)
# print the JSON string representation of the object
print(DeskAdminReportsResponseMeta.to_json())

# convert the object into a dict
desk_admin_reports_response_meta_dict = desk_admin_reports_response_meta_instance.to_dict()
# create an instance of DeskAdminReportsResponseMeta from a dict
desk_admin_reports_response_meta_from_dict = DeskAdminReportsResponseMeta.from_dict(desk_admin_reports_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


