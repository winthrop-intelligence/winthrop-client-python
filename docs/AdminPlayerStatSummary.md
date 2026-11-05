# AdminPlayerStatSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**position** | **str** |  | [optional] 
**player_number** | **int** |  | [optional] 
**average_stars** | **float** |  | [optional] 
**overall_ranking** | **int** |  | [optional] 
**position_ranking** | **int** |  | [optional] 
**points** | **int** |  | [optional] 
**rebounds** | **int** |  | [optional] 
**assists** | **int** |  | [optional] 
**eligibility_year** | **int** |  | [optional] 
**eligible** | **str** |  | [optional] 
**recruit_year** | **bool** |  | [optional] 
**transfer_year** | **bool** |  | [optional] 
**last_season** | **bool** |  | [optional] 
**season_id** | **int** |  | [optional] 
**season_school** | **str** |  | [optional] 
**season_sport** | **str** |  | [optional] 
**season_year** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_stat_summary import AdminPlayerStatSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerStatSummary from a JSON string
admin_player_stat_summary_instance = AdminPlayerStatSummary.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerStatSummary.to_json())

# convert the object into a dict
admin_player_stat_summary_dict = admin_player_stat_summary_instance.to_dict()
# create an instance of AdminPlayerStatSummary from a dict
admin_player_stat_summary_from_dict = AdminPlayerStatSummary.from_dict(admin_player_stat_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


