# WireChangeCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**avatar** | [**Avatar**](Avatar.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.wire_change_coach import WireChangeCoach

# TODO update the JSON string below
json = "{}"
# create an instance of WireChangeCoach from a JSON string
wire_change_coach_instance = WireChangeCoach.from_json(json)
# print the JSON string representation of the object
print(WireChangeCoach.to_json())

# convert the object into a dict
wire_change_coach_dict = wire_change_coach_instance.to_dict()
# create an instance of WireChangeCoach from a dict
wire_change_coach_from_dict = WireChangeCoach.from_dict(wire_change_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


