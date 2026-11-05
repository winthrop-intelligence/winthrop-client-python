# AdminRankingsEditorSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**directors_cup_ranking** | **int** |  | [optional] 
**usnwr_ranking** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_rankings_editor_school import AdminRankingsEditorSchool

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRankingsEditorSchool from a JSON string
admin_rankings_editor_school_instance = AdminRankingsEditorSchool.from_json(json)
# print the JSON string representation of the object
print(AdminRankingsEditorSchool.to_json())

# convert the object into a dict
admin_rankings_editor_school_dict = admin_rankings_editor_school_instance.to_dict()
# create an instance of AdminRankingsEditorSchool from a dict
admin_rankings_editor_school_from_dict = AdminRankingsEditorSchool.from_dict(admin_rankings_editor_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


