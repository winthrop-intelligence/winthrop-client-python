# ContactSearchEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**sport_name_display** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.contact_search_entry import ContactSearchEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ContactSearchEntry from a JSON string
contact_search_entry_instance = ContactSearchEntry.from_json(json)
# print the JSON string representation of the object
print(ContactSearchEntry.to_json())

# convert the object into a dict
contact_search_entry_dict = contact_search_entry_instance.to_dict()
# create an instance of ContactSearchEntry from a dict
contact_search_entry_from_dict = ContactSearchEntry.from_dict(contact_search_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


