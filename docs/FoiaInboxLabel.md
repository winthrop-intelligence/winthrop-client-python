# FoiaInboxLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_label import FoiaInboxLabel

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxLabel from a JSON string
foia_inbox_label_instance = FoiaInboxLabel.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxLabel.to_json())

# convert the object into a dict
foia_inbox_label_dict = foia_inbox_label_instance.to_dict()
# create an instance of FoiaInboxLabel from a dict
foia_inbox_label_from_dict = FoiaInboxLabel.from_dict(foia_inbox_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


