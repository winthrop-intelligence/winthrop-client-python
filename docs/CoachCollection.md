# CoachCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Coach]**](Coach.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_collection import CoachCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCollection from a JSON string
coach_collection_instance = CoachCollection.from_json(json)
# print the JSON string representation of the object
print CoachCollection.to_json()

# convert the object into a dict
coach_collection_dict = coach_collection_instance.to_dict()
# create an instance of CoachCollection from a dict
coach_collection_form_dict = coach_collection.from_dict(coach_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


