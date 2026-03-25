# CoachCoworkerHistoryTab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_see_coworker_history** | **bool** |  | 
**tenures** | [**List[CoworkerTenure]**](CoworkerTenure.md) |  | 

## Example

```python
from winthrop_client_python.models.coach_coworker_history_tab import CoachCoworkerHistoryTab

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCoworkerHistoryTab from a JSON string
coach_coworker_history_tab_instance = CoachCoworkerHistoryTab.from_json(json)
# print the JSON string representation of the object
print(CoachCoworkerHistoryTab.to_json())

# convert the object into a dict
coach_coworker_history_tab_dict = coach_coworker_history_tab_instance.to_dict()
# create an instance of CoachCoworkerHistoryTab from a dict
coach_coworker_history_tab_from_dict = CoachCoworkerHistoryTab.from_dict(coach_coworker_history_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


