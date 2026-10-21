# AdminConferenceshipsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminConferenceship]**](AdminConferenceship.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_conferenceships_list import AdminConferenceshipsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConferenceshipsList from a JSON string
admin_conferenceships_list_instance = AdminConferenceshipsList.from_json(json)
# print the JSON string representation of the object
print(AdminConferenceshipsList.to_json())

# convert the object into a dict
admin_conferenceships_list_dict = admin_conferenceships_list_instance.to_dict()
# create an instance of AdminConferenceshipsList from a dict
admin_conferenceships_list_from_dict = AdminConferenceshipsList.from_dict(admin_conferenceships_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


