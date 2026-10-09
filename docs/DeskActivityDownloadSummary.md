# DeskActivityDownloadSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_downloaders** | **int** |  | 
**total_downloads** | **int** |  | 
**file_groups** | **int** | Individual file groups, or user groups for Download All; pagination counts these rows. | 

## Example

```python
from winthrop_client_python.models.desk_activity_download_summary import DeskActivityDownloadSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeskActivityDownloadSummary from a JSON string
desk_activity_download_summary_instance = DeskActivityDownloadSummary.from_json(json)
# print the JSON string representation of the object
print(DeskActivityDownloadSummary.to_json())

# convert the object into a dict
desk_activity_download_summary_dict = desk_activity_download_summary_instance.to_dict()
# create an instance of DeskActivityDownloadSummary from a dict
desk_activity_download_summary_from_dict = DeskActivityDownloadSummary.from_dict(desk_activity_download_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


