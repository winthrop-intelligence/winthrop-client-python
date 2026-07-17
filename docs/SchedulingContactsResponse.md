# SchedulingContactsResponse

WINAD-10119 Scheduling Contacts directory payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[SchedulingContact]**](SchedulingContact.md) |  | 
**viewer_school_name** | **str** | The viewer&#39;s own school name, or null for non-school accounts. | 
**viewer_school_logo_url** | **str** | The viewer&#39;s own school logo URL (small variant) — the scheduling Message dialog sender badge; null when no school or no logo. | 
**viewer_has_location** | **bool** | Whether the viewer&#39;s school has coordinates (Near me availability). | 

## Example

```python
from winthrop_client_python.models.scheduling_contacts_response import SchedulingContactsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingContactsResponse from a JSON string
scheduling_contacts_response_instance = SchedulingContactsResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulingContactsResponse.to_json())

# convert the object into a dict
scheduling_contacts_response_dict = scheduling_contacts_response_instance.to_dict()
# create an instance of SchedulingContactsResponse from a dict
scheduling_contacts_response_from_dict = SchedulingContactsResponse.from_dict(scheduling_contacts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


