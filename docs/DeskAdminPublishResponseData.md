# DeskAdminPublishResponseData

The 06.4 receipt (DeskPublishReceipt) plus the version minted — never the body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**DeskAdminPublishResponseDataReport**](DeskAdminPublishResponseDataReport.md) |  | 
**client** | **str** |  | 
**turnaround_label** | **str** |  | 
**requester_name** | **str** |  | 
**version** | [**DeskAdminVersion**](DeskAdminVersion.md) |  | 
**notified** | **bool** | Whether this publish queued the delivery email (async; not a delivery receipt) | 
**notified_count** | **int** | How many people on the client&#39;s account it went to | 
**warnings** | [**List[DeskFinding]**](DeskFinding.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_publish_response_data import DeskAdminPublishResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminPublishResponseData from a JSON string
desk_admin_publish_response_data_instance = DeskAdminPublishResponseData.from_json(json)
# print the JSON string representation of the object
print(DeskAdminPublishResponseData.to_json())

# convert the object into a dict
desk_admin_publish_response_data_dict = desk_admin_publish_response_data_instance.to_dict()
# create an instance of DeskAdminPublishResponseData from a dict
desk_admin_publish_response_data_from_dict = DeskAdminPublishResponseData.from_dict(desk_admin_publish_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


