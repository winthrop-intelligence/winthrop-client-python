# AsstCoachSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**pool_total** | **int** |  | [optional] 
**coaches** | [**List[AsstCoachEntry]**](AsstCoachEntry.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.asst_coach_school import AsstCoachSchool

# TODO update the JSON string below
json = "{}"
# create an instance of AsstCoachSchool from a JSON string
asst_coach_school_instance = AsstCoachSchool.from_json(json)
# print the JSON string representation of the object
print(AsstCoachSchool.to_json())

# convert the object into a dict
asst_coach_school_dict = asst_coach_school_instance.to_dict()
# create an instance of AsstCoachSchool from a dict
asst_coach_school_from_dict = AsstCoachSchool.from_dict(asst_coach_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


