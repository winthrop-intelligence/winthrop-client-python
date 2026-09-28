# SchedulingContactPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** | The first ranked assignment&#39;s title (WINAD-10522); null when none. | 
**assignments** | [**List[PersonAssignment]**](PersonAssignment.md) | The coach&#39;s current-season positions at this school, ranked primary first: the directory sport&#39;s positions, or every sport&#39;s when the coach holds none in it. | [optional] 
**coach_id** | **int** |  | 
**photo_url** | **str** | Cropped coach avatar path; null when the coach has no image. | 

## Example

```python
from winthrop_client_python.models.scheduling_contact_person import SchedulingContactPerson

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingContactPerson from a JSON string
scheduling_contact_person_instance = SchedulingContactPerson.from_json(json)
# print the JSON string representation of the object
print(SchedulingContactPerson.to_json())

# convert the object into a dict
scheduling_contact_person_dict = scheduling_contact_person_instance.to_dict()
# create an instance of SchedulingContactPerson from a dict
scheduling_contact_person_from_dict = SchedulingContactPerson.from_dict(scheduling_contact_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


