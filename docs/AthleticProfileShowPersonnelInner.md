# AthleticProfileShowPersonnelInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**position_name** | **str** |  | [optional] 
**departing** | **bool** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**salary_cents** | **int** |  | [optional] 
**salary_display** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_personnel_inner import AthleticProfileShowPersonnelInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowPersonnelInner from a JSON string
athletic_profile_show_personnel_inner_instance = AthleticProfileShowPersonnelInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowPersonnelInner.to_json())

# convert the object into a dict
athletic_profile_show_personnel_inner_dict = athletic_profile_show_personnel_inner_instance.to_dict()
# create an instance of AthleticProfileShowPersonnelInner from a dict
athletic_profile_show_personnel_inner_from_dict = AthleticProfileShowPersonnelInner.from_dict(athletic_profile_show_personnel_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


