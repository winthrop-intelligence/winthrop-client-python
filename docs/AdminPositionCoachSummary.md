# AdminPositionCoachSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_position_coach_summary import AdminPositionCoachSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionCoachSummary from a JSON string
admin_position_coach_summary_instance = AdminPositionCoachSummary.from_json(json)
# print the JSON string representation of the object
print(AdminPositionCoachSummary.to_json())

# convert the object into a dict
admin_position_coach_summary_dict = admin_position_coach_summary_instance.to_dict()
# create an instance of AdminPositionCoachSummary from a dict
admin_position_coach_summary_from_dict = AdminPositionCoachSummary.from_dict(admin_position_coach_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


