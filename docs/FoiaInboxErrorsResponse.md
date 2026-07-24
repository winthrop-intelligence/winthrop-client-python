# FoiaInboxErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_errors_response import FoiaInboxErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxErrorsResponse from a JSON string
foia_inbox_errors_response_instance = FoiaInboxErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxErrorsResponse.to_json())

# convert the object into a dict
foia_inbox_errors_response_dict = foia_inbox_errors_response_instance.to_dict()
# create an instance of FoiaInboxErrorsResponse from a dict
foia_inbox_errors_response_from_dict = FoiaInboxErrorsResponse.from_dict(foia_inbox_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


