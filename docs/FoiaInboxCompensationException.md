# FoiaInboxCompensationException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_item_id** | **int** |  | 
**role** | **str** |  | 
**actions** | **List[str]** |  | 
**expected_requested_item** | [**FoiaInboxExpectedRequestedItem**](FoiaInboxExpectedRequestedItem.md) |  | 
**expected_compensation** | [**FoiaInboxExpectedCompensation**](FoiaInboxExpectedCompensation.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_compensation_exception import FoiaInboxCompensationException

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxCompensationException from a JSON string
foia_inbox_compensation_exception_instance = FoiaInboxCompensationException.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxCompensationException.to_json())

# convert the object into a dict
foia_inbox_compensation_exception_dict = foia_inbox_compensation_exception_instance.to_dict()
# create an instance of FoiaInboxCompensationException from a dict
foia_inbox_compensation_exception_from_dict = FoiaInboxCompensationException.from_dict(foia_inbox_compensation_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


