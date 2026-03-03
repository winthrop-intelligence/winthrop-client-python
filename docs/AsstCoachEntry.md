# AsstCoachEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**total_comp** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.asst_coach_entry import AsstCoachEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AsstCoachEntry from a JSON string
asst_coach_entry_instance = AsstCoachEntry.from_json(json)
# print the JSON string representation of the object
print(AsstCoachEntry.to_json())

# convert the object into a dict
asst_coach_entry_dict = asst_coach_entry_instance.to_dict()
# create an instance of AsstCoachEntry from a dict
asst_coach_entry_from_dict = AsstCoachEntry.from_dict(asst_coach_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


