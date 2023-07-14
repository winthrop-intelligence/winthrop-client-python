# FoiaLabelCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FoiaLabel]**](FoiaLabel.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_label_collection import FoiaLabelCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaLabelCollection from a JSON string
foia_label_collection_instance = FoiaLabelCollection.from_json(json)
# print the JSON string representation of the object
print FoiaLabelCollection.to_json()

# convert the object into a dict
foia_label_collection_dict = foia_label_collection_instance.to_dict()
# create an instance of FoiaLabelCollection from a dict
foia_label_collection_form_dict = foia_label_collection.from_dict(foia_label_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


