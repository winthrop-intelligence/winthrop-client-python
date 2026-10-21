# AdminPositionSeasonSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**year** | **int** |  | 
**school** | [**AdminPositionSchoolSummary**](AdminPositionSchoolSummary.md) |  | 
**sport** | [**AdminPositionSportSummary**](AdminPositionSportSummary.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_position_season_summary import AdminPositionSeasonSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionSeasonSummary from a JSON string
admin_position_season_summary_instance = AdminPositionSeasonSummary.from_json(json)
# print the JSON string representation of the object
print(AdminPositionSeasonSummary.to_json())

# convert the object into a dict
admin_position_season_summary_dict = admin_position_season_summary_instance.to_dict()
# create an instance of AdminPositionSeasonSummary from a dict
admin_position_season_summary_from_dict = AdminPositionSeasonSummary.from_dict(admin_position_season_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


