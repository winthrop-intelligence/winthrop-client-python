# ContactSearchCoachOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_name** | **str** |  | [optional] 
**coaches** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**sports** | [**List[ContactSearchCoachOptionsSportsInner]**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.contact_search_coach_options import ContactSearchCoachOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ContactSearchCoachOptions from a JSON string
contact_search_coach_options_instance = ContactSearchCoachOptions.from_json(json)
# print the JSON string representation of the object
print(ContactSearchCoachOptions.to_json())

# convert the object into a dict
contact_search_coach_options_dict = contact_search_coach_options_instance.to_dict()
# create an instance of ContactSearchCoachOptions from a dict
contact_search_coach_options_from_dict = ContactSearchCoachOptions.from_dict(contact_search_coach_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


