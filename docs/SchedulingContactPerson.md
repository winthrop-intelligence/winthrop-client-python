# SchedulingContactPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** | Current-season primary title at this school, ranked by the lowest non-null position-type ord. A typed custom title takes precedence over ordered position-type labels; null without a title. | 
**assignments** | [**List[PersonAssignment]**](PersonAssignment.md) | Current-season assignments at this contact&#39;s school, in the shared person-summary ranking order, primary first. Sport-specific viewers receive only their permitted sports. Includes each distinct position once, across sports, regardless of how many position-type labels it has. Empty without positions or a linked coach. Powers the additional-job count and complete disclosure list. | 
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


