# DeskActivityDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**name** | **str** | Current WinAD name, or Removed user. No PostHog personal details are queried. | 
**email** | **str** |  | 
**status** | **str** |  | 
**current_access** | **bool** |  | 
**downloads** | **int** |  | 
**first_downloaded_at** | **datetime** |  | 
**last_downloaded_at** | **datetime** |  | 
**file_name** | **str** | Observed filename, null when absent or for an across-version ZIP group. | 
**file_label** | **str** | Observed filename, &#39;[Unknown file]&#39;, or &#39;All files (ZIP)&#39;. | 
**file_type** | **str** | Trimmed lowercase event type; ZIP appears only in Download All. Missing type is unknown coverage. | 
**artifact_id** | **str** |  | 
**artifact_version_id** | **str** |  | 
**version_number** | **int** | Observed report version, never inferred. Null for Download All across versions. | 
**identity_context** | **str** |  | 
**version_context** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_activity_download import DeskActivityDownload

# TODO update the JSON string below
json = "{}"
# create an instance of DeskActivityDownload from a JSON string
desk_activity_download_instance = DeskActivityDownload.from_json(json)
# print the JSON string representation of the object
print(DeskActivityDownload.to_json())

# convert the object into a dict
desk_activity_download_dict = desk_activity_download_instance.to_dict()
# create an instance of DeskActivityDownload from a dict
desk_activity_download_from_dict = DeskActivityDownload.from_dict(desk_activity_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


