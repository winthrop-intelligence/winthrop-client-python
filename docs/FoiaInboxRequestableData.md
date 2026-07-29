# FoiaInboxRequestableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**contract_status** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**positions_sha256** | **str** |  | [optional] 
**positions** | [**List[FoiaInboxExpectedPosition]**](FoiaInboxExpectedPosition.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_requestable_data import FoiaInboxRequestableData

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxRequestableData from a JSON string
foia_inbox_requestable_data_instance = FoiaInboxRequestableData.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxRequestableData.to_json())

# convert the object into a dict
foia_inbox_requestable_data_dict = foia_inbox_requestable_data_instance.to_dict()
# create an instance of FoiaInboxRequestableData from a dict
foia_inbox_requestable_data_from_dict = FoiaInboxRequestableData.from_dict(foia_inbox_requestable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


