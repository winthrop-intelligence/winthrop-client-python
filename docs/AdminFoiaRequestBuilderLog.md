# AdminFoiaRequestBuilderLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foia_label_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**builder_type** | **str** |  | [optional] 
**initialize_at** | **datetime** |  | [optional] 
**complete_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**foia_label_name** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**has_detail_items** | **bool** |  | [optional] 
**detail** | **object** | Computed per-school breakdown of requested items, sent dates, and compensation status for this builder run | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_builder_log import AdminFoiaRequestBuilderLog

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestBuilderLog from a JSON string
admin_foia_request_builder_log_instance = AdminFoiaRequestBuilderLog.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestBuilderLog.to_json())

# convert the object into a dict
admin_foia_request_builder_log_dict = admin_foia_request_builder_log_instance.to_dict()
# create an instance of AdminFoiaRequestBuilderLog from a dict
admin_foia_request_builder_log_from_dict = AdminFoiaRequestBuilderLog.from_dict(admin_foia_request_builder_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


