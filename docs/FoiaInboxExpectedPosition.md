# FoiaInboxExpectedPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**position_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_expected_position import FoiaInboxExpectedPosition

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxExpectedPosition from a JSON string
foia_inbox_expected_position_instance = FoiaInboxExpectedPosition.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxExpectedPosition.to_json())

# convert the object into a dict
foia_inbox_expected_position_dict = foia_inbox_expected_position_instance.to_dict()
# create an instance of FoiaInboxExpectedPosition from a dict
foia_inbox_expected_position_from_dict = FoiaInboxExpectedPosition.from_dict(foia_inbox_expected_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


