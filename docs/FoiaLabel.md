# FoiaLabel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**archived** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_label import FoiaLabel

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaLabel from a JSON string
foia_label_instance = FoiaLabel.from_json(json)
# print the JSON string representation of the object
print FoiaLabel.to_json()

# convert the object into a dict
foia_label_dict = foia_label_instance.to_dict()
# create an instance of FoiaLabel from a dict
foia_label_form_dict = foia_label.from_dict(foia_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


