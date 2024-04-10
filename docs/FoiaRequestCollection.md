# FoiaRequestCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FoiaRequest]**](FoiaRequest.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_request_collection import FoiaRequestCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestCollection from a JSON string
foia_request_collection_instance = FoiaRequestCollection.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestCollection.to_json())

# convert the object into a dict
foia_request_collection_dict = foia_request_collection_instance.to_dict()
# create an instance of FoiaRequestCollection from a dict
foia_request_collection_form_dict = foia_request_collection.from_dict(foia_request_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


