# AthleticProfileShowContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**position_name** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_contacts_inner import AthleticProfileShowContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowContactsInner from a JSON string
athletic_profile_show_contacts_inner_instance = AthleticProfileShowContactsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowContactsInner.to_json())

# convert the object into a dict
athletic_profile_show_contacts_inner_dict = athletic_profile_show_contacts_inner_instance.to_dict()
# create an instance of AthleticProfileShowContactsInner from a dict
athletic_profile_show_contacts_inner_from_dict = AthleticProfileShowContactsInner.from_dict(athletic_profile_show_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


