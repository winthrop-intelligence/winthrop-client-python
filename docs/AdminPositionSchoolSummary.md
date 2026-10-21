# AdminPositionSchoolSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_position_school_summary import AdminPositionSchoolSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionSchoolSummary from a JSON string
admin_position_school_summary_instance = AdminPositionSchoolSummary.from_json(json)
# print the JSON string representation of the object
print(AdminPositionSchoolSummary.to_json())

# convert the object into a dict
admin_position_school_summary_dict = admin_position_school_summary_instance.to_dict()
# create an instance of AdminPositionSchoolSummary from a dict
admin_position_school_summary_from_dict = AdminPositionSchoolSummary.from_dict(admin_position_school_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


