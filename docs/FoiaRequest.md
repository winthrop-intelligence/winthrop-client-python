# FoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | 
**created_by_id** | **int** |  | [optional] 
**updated_by_id** | **int** |  | [optional] 
**state** | **str** |  | 
**foia_label_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_request import FoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequest from a JSON string
foia_request_instance = FoiaRequest.from_json(json)
# print the JSON string representation of the object
print(FoiaRequest.to_json())

# convert the object into a dict
foia_request_dict = foia_request_instance.to_dict()
# create an instance of FoiaRequest from a dict
foia_request_form_dict = foia_request.from_dict(foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


