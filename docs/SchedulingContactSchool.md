# SchedulingContactSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**schedule_profile_eligible** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.scheduling_contact_school import SchedulingContactSchool

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingContactSchool from a JSON string
scheduling_contact_school_instance = SchedulingContactSchool.from_json(json)
# print the JSON string representation of the object
print(SchedulingContactSchool.to_json())

# convert the object into a dict
scheduling_contact_school_dict = scheduling_contact_school_instance.to_dict()
# create an instance of SchedulingContactSchool from a dict
scheduling_contact_school_from_dict = SchedulingContactSchool.from_dict(scheduling_contact_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


