# CoachCompensation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**estimated** | **bool** |  | [optional] 
**salary** | **float** | The base salary (rounded to 2 decimal places) | [optional] 
**year** | **int** |  | [optional] 
**coli_salary** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation import CoachCompensation

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensation from a JSON string
coach_compensation_instance = CoachCompensation.from_json(json)
# print the JSON string representation of the object
print(CoachCompensation.to_json())

# convert the object into a dict
coach_compensation_dict = coach_compensation_instance.to_dict()
# create an instance of CoachCompensation from a dict
coach_compensation_form_dict = coach_compensation.from_dict(coach_compensation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


