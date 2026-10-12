# DeskActivitySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_viewers** | **int** |  | 
**total_opens** | **int** |  | 

## Example

```python
from winthrop_client_python.models.desk_activity_summary import DeskActivitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeskActivitySummary from a JSON string
desk_activity_summary_instance = DeskActivitySummary.from_json(json)
# print the JSON string representation of the object
print(DeskActivitySummary.to_json())

# convert the object into a dict
desk_activity_summary_dict = desk_activity_summary_instance.to_dict()
# create an instance of DeskActivitySummary from a dict
desk_activity_summary_from_dict = DeskActivitySummary.from_dict(desk_activity_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


