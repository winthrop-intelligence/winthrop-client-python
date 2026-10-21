# AdminPositionTypeGroupSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**name_display** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_position_type_group_summary import AdminPositionTypeGroupSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionTypeGroupSummary from a JSON string
admin_position_type_group_summary_instance = AdminPositionTypeGroupSummary.from_json(json)
# print the JSON string representation of the object
print(AdminPositionTypeGroupSummary.to_json())

# convert the object into a dict
admin_position_type_group_summary_dict = admin_position_type_group_summary_instance.to_dict()
# create an instance of AdminPositionTypeGroupSummary from a dict
admin_position_type_group_summary_from_dict = AdminPositionTypeGroupSummary.from_dict(admin_position_type_group_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


