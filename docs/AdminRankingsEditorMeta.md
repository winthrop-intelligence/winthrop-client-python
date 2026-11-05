# AdminRankingsEditorMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**years** | **List[int]** |  | [optional] 
**conferences** | [**List[AdminRankingsEditorConference]**](AdminRankingsEditorConference.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_rankings_editor_meta import AdminRankingsEditorMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRankingsEditorMeta from a JSON string
admin_rankings_editor_meta_instance = AdminRankingsEditorMeta.from_json(json)
# print the JSON string representation of the object
print(AdminRankingsEditorMeta.to_json())

# convert the object into a dict
admin_rankings_editor_meta_dict = admin_rankings_editor_meta_instance.to_dict()
# create an instance of AdminRankingsEditorMeta from a dict
admin_rankings_editor_meta_from_dict = AdminRankingsEditorMeta.from_dict(admin_rankings_editor_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


