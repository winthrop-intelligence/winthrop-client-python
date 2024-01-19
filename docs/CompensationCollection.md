# CompensationCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Compensation]**](Compensation.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.compensation_collection import CompensationCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationCollection from a JSON string
compensation_collection_instance = CompensationCollection.from_json(json)
# print the JSON string representation of the object
print CompensationCollection.to_json()

# convert the object into a dict
compensation_collection_dict = compensation_collection_instance.to_dict()
# create an instance of CompensationCollection from a dict
compensation_collection_form_dict = compensation_collection.from_dict(compensation_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


