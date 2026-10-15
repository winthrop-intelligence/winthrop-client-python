# AdminCoachPositionsBySportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | [optional] 
**sport_name_display** | **str** |  | [optional] 
**position_count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_positions_by_sport_inner import AdminCoachPositionsBySportInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachPositionsBySportInner from a JSON string
admin_coach_positions_by_sport_inner_instance = AdminCoachPositionsBySportInner.from_json(json)
# print the JSON string representation of the object
print(AdminCoachPositionsBySportInner.to_json())

# convert the object into a dict
admin_coach_positions_by_sport_inner_dict = admin_coach_positions_by_sport_inner_instance.to_dict()
# create an instance of AdminCoachPositionsBySportInner from a dict
admin_coach_positions_by_sport_inner_from_dict = AdminCoachPositionsBySportInner.from_dict(admin_coach_positions_by_sport_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


