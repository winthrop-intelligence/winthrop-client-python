# AdminPositionSportSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**name_display** | **str** |  | 
**admin** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.admin_position_sport_summary import AdminPositionSportSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionSportSummary from a JSON string
admin_position_sport_summary_instance = AdminPositionSportSummary.from_json(json)
# print the JSON string representation of the object
print(AdminPositionSportSummary.to_json())

# convert the object into a dict
admin_position_sport_summary_dict = admin_position_sport_summary_instance.to_dict()
# create an instance of AdminPositionSportSummary from a dict
admin_position_sport_summary_from_dict = AdminPositionSportSummary.from_dict(admin_position_sport_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


