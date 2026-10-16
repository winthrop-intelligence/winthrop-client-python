# AdminEligibleCoachOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_eligible_coach_option import AdminEligibleCoachOption

# TODO update the JSON string below
json = "{}"
# create an instance of AdminEligibleCoachOption from a JSON string
admin_eligible_coach_option_instance = AdminEligibleCoachOption.from_json(json)
# print the JSON string representation of the object
print(AdminEligibleCoachOption.to_json())

# convert the object into a dict
admin_eligible_coach_option_dict = admin_eligible_coach_option_instance.to_dict()
# create an instance of AdminEligibleCoachOption from a dict
admin_eligible_coach_option_from_dict = AdminEligibleCoachOption.from_dict(admin_eligible_coach_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


