# AdminPositionCompensationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**calculated_guaranteed_comp_cents** | **int** |  | 

## Example

```python
from winthrop_client_python.models.admin_position_compensation_summary import AdminPositionCompensationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPositionCompensationSummary from a JSON string
admin_position_compensation_summary_instance = AdminPositionCompensationSummary.from_json(json)
# print the JSON string representation of the object
print(AdminPositionCompensationSummary.to_json())

# convert the object into a dict
admin_position_compensation_summary_dict = admin_position_compensation_summary_instance.to_dict()
# create an instance of AdminPositionCompensationSummary from a dict
admin_position_compensation_summary_from_dict = AdminPositionCompensationSummary.from_dict(admin_position_compensation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


