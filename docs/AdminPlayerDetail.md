# AdminPlayerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**external_code** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**height** | **int** | Raw editable height in inches | [optional] 
**height_display** | **str** | Formatted height, e.g. \&quot;6&#39;9\&quot; | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**player_stats** | [**List[AdminPlayerStatSummary]**](AdminPlayerStatSummary.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_detail import AdminPlayerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerDetail from a JSON string
admin_player_detail_instance = AdminPlayerDetail.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerDetail.to_json())

# convert the object into a dict
admin_player_detail_dict = admin_player_detail_instance.to_dict()
# create an instance of AdminPlayerDetail from a dict
admin_player_detail_from_dict = AdminPlayerDetail.from_dict(admin_player_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


