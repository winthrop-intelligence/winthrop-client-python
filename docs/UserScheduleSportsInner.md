# UserScheduleSportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.user_schedule_sports_inner import UserScheduleSportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserScheduleSportsInner from a JSON string
user_schedule_sports_inner_instance = UserScheduleSportsInner.from_json(json)
# print the JSON string representation of the object
print(UserScheduleSportsInner.to_json())

# convert the object into a dict
user_schedule_sports_inner_dict = user_schedule_sports_inner_instance.to_dict()
# create an instance of UserScheduleSportsInner from a dict
user_schedule_sports_inner_from_dict = UserScheduleSportsInner.from_dict(user_schedule_sports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


