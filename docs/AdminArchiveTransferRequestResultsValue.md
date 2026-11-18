# AdminArchiveTransferRequestResultsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_archive_transfer_request_results_value import AdminArchiveTransferRequestResultsValue

# TODO update the JSON string below
json = "{}"
# create an instance of AdminArchiveTransferRequestResultsValue from a JSON string
admin_archive_transfer_request_results_value_instance = AdminArchiveTransferRequestResultsValue.from_json(json)
# print the JSON string representation of the object
print(AdminArchiveTransferRequestResultsValue.to_json())

# convert the object into a dict
admin_archive_transfer_request_results_value_dict = admin_archive_transfer_request_results_value_instance.to_dict()
# create an instance of AdminArchiveTransferRequestResultsValue from a dict
admin_archive_transfer_request_results_value_from_dict = AdminArchiveTransferRequestResultsValue.from_dict(admin_archive_transfer_request_results_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


