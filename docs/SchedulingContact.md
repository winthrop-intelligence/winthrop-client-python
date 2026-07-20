# SchedulingContact

One school's primary scheduling contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**school** | [**SchedulingContactSchool**](SchedulingContactSchool.md) |  | 
**conference** | [**SchedulingContactConference**](SchedulingContactConference.md) |  | 
**person** | [**SchedulingContactPerson**](SchedulingContactPerson.md) |  | 
**cell_phone** | **str** |  | 
**office_phone** | **str** |  | 
**email** | **str** |  | 
**verified** | **bool** |  | 
**verified_at** | **date** |  | 
**distance_miles** | **int** | Miles from the viewer&#39;s school; null when either school lacks a location. | 
**open_posts_count** | **int** |  | 

## Example

```python
from winthrop_client_python.models.scheduling_contact import SchedulingContact

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingContact from a JSON string
scheduling_contact_instance = SchedulingContact.from_json(json)
# print the JSON string representation of the object
print(SchedulingContact.to_json())

# convert the object into a dict
scheduling_contact_dict = scheduling_contact_instance.to_dict()
# create an instance of SchedulingContact from a dict
scheduling_contact_from_dict = SchedulingContact.from_dict(scheduling_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


