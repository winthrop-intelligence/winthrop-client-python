# SchedulingContactConference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**abbreviation** | **str** |  | 
**tier** | **str** |  | 

## Example

```python
from winthrop_client_python.models.scheduling_contact_conference import SchedulingContactConference

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingContactConference from a JSON string
scheduling_contact_conference_instance = SchedulingContactConference.from_json(json)
# print the JSON string representation of the object
print(SchedulingContactConference.to_json())

# convert the object into a dict
scheduling_contact_conference_dict = scheduling_contact_conference_instance.to_dict()
# create an instance of SchedulingContactConference from a dict
scheduling_contact_conference_from_dict = SchedulingContactConference.from_dict(scheduling_contact_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


