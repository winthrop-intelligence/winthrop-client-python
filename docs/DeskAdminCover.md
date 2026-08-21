# DeskAdminCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**headline_stats** | [**List[DeskHeadlineStat]**](DeskHeadlineStat.md) |  | [optional] 
**cover_treatment** | **str** |  | [optional] 
**cover_kicker** | **str** | Defaults to \&quot;THE DESK · PREPARED FOR &lt;ACCOUNT&gt;\&quot; on create | [optional] 
**cover_numeral** | **str** |  | [optional] 
**page_count** | **int** |  | [optional] 
**push_example** | **str** |  | [optional] 
**rerun_cadence** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.desk_admin_cover import DeskAdminCover

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminCover from a JSON string
desk_admin_cover_instance = DeskAdminCover.from_json(json)
# print the JSON string representation of the object
print(DeskAdminCover.to_json())

# convert the object into a dict
desk_admin_cover_dict = desk_admin_cover_instance.to_dict()
# create an instance of DeskAdminCover from a dict
desk_admin_cover_from_dict = DeskAdminCover.from_dict(desk_admin_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


