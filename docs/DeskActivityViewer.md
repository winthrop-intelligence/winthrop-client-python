# DeskActivityViewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**name** | **str** | Current WinAD name, or Removed user. No PostHog personal details are queried. | 
**email** | **str** |  | 
**status** | **str** |  | 
**current_access** | **bool** | Current reader eligibility for this live report; historical opens do not grant access. | 
**opens** | **int** |  | 
**first_viewed_at** | **datetime** |  | 
**last_viewed_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.desk_activity_viewer import DeskActivityViewer

# TODO update the JSON string below
json = "{}"
# create an instance of DeskActivityViewer from a JSON string
desk_activity_viewer_instance = DeskActivityViewer.from_json(json)
# print the JSON string representation of the object
print(DeskActivityViewer.to_json())

# convert the object into a dict
desk_activity_viewer_dict = desk_activity_viewer_instance.to_dict()
# create an instance of DeskActivityViewer from a dict
desk_activity_viewer_from_dict = DeskActivityViewer.from_dict(desk_activity_viewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


