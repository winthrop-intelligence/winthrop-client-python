# AdminRankingsEditor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminRankingsEditorMeta**](AdminRankingsEditorMeta.md) |  | [optional] 
**data** | [**AdminRankingsEditorData**](AdminRankingsEditorData.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_rankings_editor import AdminRankingsEditor

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRankingsEditor from a JSON string
admin_rankings_editor_instance = AdminRankingsEditor.from_json(json)
# print the JSON string representation of the object
print(AdminRankingsEditor.to_json())

# convert the object into a dict
admin_rankings_editor_dict = admin_rankings_editor_instance.to_dict()
# create an instance of AdminRankingsEditor from a dict
admin_rankings_editor_from_dict = AdminRankingsEditor.from_dict(admin_rankings_editor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


