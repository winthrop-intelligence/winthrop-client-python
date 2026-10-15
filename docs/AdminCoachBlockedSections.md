# AdminCoachBlockedSections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensations** | [**AdminCoachBlockedSectionsCompensations**](AdminCoachBlockedSectionsCompensations.md) |  | [optional] 
**contracts** | [**AdminCoachBlockedSectionsCompensations**](AdminCoachBlockedSectionsCompensations.md) |  | [optional] 
**income_reports** | [**AdminCoachBlockedSectionsCompensations**](AdminCoachBlockedSectionsCompensations.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_blocked_sections import AdminCoachBlockedSections

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachBlockedSections from a JSON string
admin_coach_blocked_sections_instance = AdminCoachBlockedSections.from_json(json)
# print the JSON string representation of the object
print(AdminCoachBlockedSections.to_json())

# convert the object into a dict
admin_coach_blocked_sections_dict = admin_coach_blocked_sections_instance.to_dict()
# create an instance of AdminCoachBlockedSections from a dict
admin_coach_blocked_sections_from_dict = AdminCoachBlockedSections.from_dict(admin_coach_blocked_sections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


