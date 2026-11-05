# AdminRankingsEditorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_id** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**year** | **str** |  | [optional] 
**schools** | [**List[AdminRankingsEditorSchool]**](AdminRankingsEditorSchool.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_rankings_editor_data import AdminRankingsEditorData

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRankingsEditorData from a JSON string
admin_rankings_editor_data_instance = AdminRankingsEditorData.from_json(json)
# print the JSON string representation of the object
print(AdminRankingsEditorData.to_json())

# convert the object into a dict
admin_rankings_editor_data_dict = admin_rankings_editor_data_instance.to_dict()
# create an instance of AdminRankingsEditorData from a dict
admin_rankings_editor_data_from_dict = AdminRankingsEditorData.from_dict(admin_rankings_editor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


