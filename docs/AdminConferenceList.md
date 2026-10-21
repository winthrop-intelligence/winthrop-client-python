# AdminConferenceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminConference]**](AdminConference.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_conference_list import AdminConferenceList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConferenceList from a JSON string
admin_conference_list_instance = AdminConferenceList.from_json(json)
# print the JSON string representation of the object
print(AdminConferenceList.to_json())

# convert the object into a dict
admin_conference_list_dict = admin_conference_list_instance.to_dict()
# create an instance of AdminConferenceList from a dict
admin_conference_list_from_dict = AdminConferenceList.from_dict(admin_conference_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


